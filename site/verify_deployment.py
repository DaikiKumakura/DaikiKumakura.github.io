"""Check deployed article URLs against the exact built artifact, with CDN retries."""
import argparse
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

NS = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}


def locations(data):
    return {node.text for node in ET.fromstring(data).findall('s:url/s:loc', NS)}


def fetch(url):
    separator = '&' if '?' in url else '?'
    request = Request(url + separator + 'publication_check=' + str(time.time_ns()),
                      headers={'User-Agent': 'Portfolio-Publication-Check', 'Cache-Control': 'no-cache'})
    with urlopen(request, timeout=15) as response:
        return response.read()


def check(dist, base_url):
    expected = {url for url in locations((dist / 'sitemap.xml').read_bytes())
                if urlsplit(url).path.startswith('/writing/')}
    live = locations(fetch(base_url + '/sitemap.xml'))
    missing = expected - live
    if missing:
        raise RuntimeError('Articles missing from live sitemap: ' + ', '.join(sorted(missing)))
    for url in sorted(expected):
        body = fetch(base_url + urlsplit(url).path)
        if b'<h1' not in body:
            raise RuntimeError('Article page has no heading: ' + url)
    print(f'PASS: {len(expected)} built article URLs are live and listed in the sitemap')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dist', type=Path, default=Path(__file__).resolve().parent / 'dist')
    parser.add_argument('--base-url', default='https://daikikumakura.github.io')
    args = parser.parse_args()
    for attempt in range(6):
        try:
            check(args.dist, args.base_url.rstrip('/'))
            return
        except Exception as error:
            print(f'Attempt {attempt + 1}/6: {error}', flush=True)
            if attempt == 5:
                raise
            time.sleep(20)


if __name__ == '__main__':
    main()
