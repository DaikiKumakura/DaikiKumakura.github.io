"""Notify IndexNow after a successful GitHub Pages deployment."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from urllib.parse import urlsplit

HOST = 'daikikumakura.github.io'
SITE_URL = f'https://{HOST}/'
KEY = '97b1692a1baf4e05a1e1ef4f47021a95'
KEY_URL = f'{SITE_URL}{KEY}.txt'
SITEMAP_URL = f'{SITE_URL}sitemap.xml'
# The package documentation sites are published under this host with their own sitemaps.
EXTRA_SITEMAPS = tuple(f'{SITE_URL}{name}/sitemap.xml' for name in ('rsemflow', 'pkident', 'retiaudit', 'rsemverse', 'bulkdeconv'))
ENDPOINT = 'https://api.indexnow.org/indexnow'


def urls_from_sitemap(xml: bytes) -> list[str]:
    root = ET.fromstring(xml)
    urls = [node.text.strip() for node in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc') if node.text]
    if not urls or any(not url.startswith(SITE_URL) for url in urls):
        raise ValueError('Sitemap contains no canonical site URLs or an unexpected host')
    return urls


def get(url: str) -> bytes:
    request = urllib.request.Request(url, headers={'User-Agent': 'DaikiKumakura.github.io deployment'})
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read()


def ready(dist: Path) -> list[str]:
    expected = urls_from_sitemap((dist / 'sitemap.xml').read_bytes())
    last_error: Exception | None = None
    for attempt in range(6):
        try:
            if get(f'{KEY_URL}?attempt={attempt}').decode().strip() != KEY:
                raise ValueError('Published IndexNow key does not match')
            if set(expected) != set(urls_from_sitemap(get(f'{SITEMAP_URL}?attempt={attempt}'))):
                raise ValueError('Published sitemap does not match the deployed artifact')
            return expected
        except (OSError, ValueError, ET.ParseError) as error:
            last_error = error
            if attempt < 5:
                time.sleep(5)
    raise RuntimeError('Published sitemap or key was not ready') from last_error


def signature(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def remote_signature(url: str, previous: dict) -> dict:
    headers = {'User-Agent': 'DaikiKumakura.github.io deployment'}
    if previous.get('etag'):
        headers['If-None-Match'] = previous['etag']
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=12) as response:
            return {'sha256': signature(response.read()), 'etag': response.headers.get('ETag')}
    except urllib.error.HTTPError as error:
        if error.code == 304 and previous.get('sha256'):
            return previous
        raise


def snapshots(dist: Path, previous: dict) -> dict:
    main = {}
    for url in ready(dist):
        path = urlsplit(url).path.lstrip('/')
        main[url] = {'sha256': signature((dist / (path or 'index.html')).read_bytes())}
    current = {SITEMAP_URL: main}
    with ThreadPoolExecutor(max_workers=8) as pool:
        for sitemap in EXTRA_SITEMAPS:
            old = previous.get(sitemap, {})
            prefix = sitemap.removesuffix('sitemap.xml')
            try:
                urls = list(dict.fromkeys(urls_from_sitemap(get(sitemap))))
                if any(not url.startswith(prefix) for url in urls):
                    raise ValueError('Unexpected URL outside documentation site')
                urls = [url for url in urls if urlsplit(url).path.rsplit('/', 1)[-1] != '404.html']
                values = pool.map(lambda url, group=old: remote_signature(url, group.get(url, {})), urls)
                current[sitemap] = dict(zip(urls, values))
            except (OSError, ValueError, ET.ParseError) as error:
                print(f'Documentation snapshot unavailable for {sitemap}: {error}')
                # A temporary fetch failure is not evidence that URLs were removed.
                if sitemap in previous:
                    current[sitemap] = old
    return current


def changed_urls(previous: dict, current: dict) -> list[str]:
    def hashes(groups):
        return {url: entry['sha256'] for group in groups.values() for url, entry in group.items()}

    old = hashes(previous)
    new = hashes(current)
    return sorted(url for url in old.keys() | new.keys() if old.get(url) != new.get(url))


def submit(urls: list[str]) -> None:
    payload = json.dumps({'host': HOST, 'key': KEY, 'keyLocation': KEY_URL, 'urlList': urls}).encode()
    request = urllib.request.Request(ENDPOINT, data=payload, headers={'Content-Type': 'application/json; charset=utf-8'}, method='POST')
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            if response.status not in (200, 202):
                raise RuntimeError(f'IndexNow returned HTTP {response.status}')
    except urllib.error.HTTPError as error:
        raise RuntimeError(f'IndexNow returned HTTP {error.code}') from error
    print(f'IndexNow accepted {len(urls)} new, changed or removed URLs')


def notify(dist: Path, state: Path) -> bool:
    try:
        previous = json.loads(state.read_text(encoding='utf-8'))
    except (FileNotFoundError, json.JSONDecodeError):
        previous = {}
    current = snapshots(dist, previous)
    urls = changed_urls(previous, current)
    if not urls:
        print('IndexNow skipped: no URL changes')
    for start in range(0, len(urls), 10_000):
        submit(urls[start:start + 10_000])
    if current == previous:
        return False
    # Advance the baseline only after every notification batch was accepted.
    state.parent.mkdir(parents=True, exist_ok=True)
    temporary = state.with_suffix('.tmp')
    temporary.write_text(json.dumps(current, sort_keys=True), encoding='utf-8')
    temporary.replace(state)
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dist', type=Path, required=True)
    parser.add_argument('--state', type=Path, required=True)
    args = parser.parse_args()
    changed = notify(args.dist, args.state)
    if output := os.environ.get('GITHUB_OUTPUT'):
        with open(output, 'a', encoding='utf-8') as handle:
            handle.write(f'state_changed={str(changed).lower()}\n')


if __name__ == '__main__':
    main()

