"""Notify IndexNow after a successful GitHub Pages deployment."""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

HOST = 'daikikumakura.github.io'
SITE_URL = f'https://{HOST}/'
KEY = '97b1692a1baf4e05a1e1ef4f47021a95'
KEY_URL = f'{SITE_URL}{KEY}.txt'
SITEMAP_URL = f'{SITE_URL}sitemap.xml'
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


def main() -> None:
    last_error: Exception | None = None
    for attempt in range(6):
        try:
            if get(f'{KEY_URL}?attempt={attempt}').decode().strip() != KEY:
                raise ValueError('Published IndexNow key does not match')
            urls = urls_from_sitemap(get(f'{SITEMAP_URL}?attempt={attempt}'))
            break
        except (OSError, ValueError, ET.ParseError) as error:
            last_error = error
            time.sleep(5)
    else:
        raise RuntimeError('Published sitemap or key was not ready') from last_error

    payload = json.dumps({'host': HOST, 'key': KEY, 'keyLocation': KEY_URL, 'urlList': urls}).encode()
    request = urllib.request.Request(ENDPOINT, data=payload, headers={'Content-Type': 'application/json; charset=utf-8'}, method='POST')
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            if response.status not in (200, 202):
                raise RuntimeError(f'IndexNow returned HTTP {response.status}')
    except urllib.error.HTTPError as error:
        raise RuntimeError(f'IndexNow returned HTTP {error.code}') from error
    print(f'IndexNow accepted {len(urls)} canonical URLs')


if __name__ == '__main__':
    main()

