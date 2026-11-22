"""Check deployed search entry points against the built artifact, with CDN retries."""
import argparse
import re
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
    expected = locations((dist / 'sitemap.xml').read_bytes())
    live = locations(fetch(base_url + '/sitemap.xml'))
    missing = expected - live
    if missing:
        raise RuntimeError('Pages missing from live sitemap: ' + ', '.join(sorted(missing)))
    unexpected = live - expected
    if unexpected:
        raise RuntimeError('Unexpected URLs in live sitemap: ' + ', '.join(sorted(unexpected)))

    priority_paths = {
        '/', '/profile.html', '/writing.html', '/writing-ja.html', '/reference.html',
        '/glossary/fixed-vs-weight-based-dosing-ja.html', '/glossary/exposure-response-ja.html',
    }
    for url in sorted(expected):
        path = urlsplit(url).path or '/'
        if not (path in priority_paths or path.startswith('/writing/')):
            continue
        body = fetch(base_url + path)
        if b'<h1' not in body:
            raise RuntimeError('Page has no heading: ' + url)
        canonicals = re.findall(rb'<link rel="canonical" href="([^"]+)">', body)
        if canonicals != [url.encode('utf-8')]:
            raise RuntimeError('Unexpected canonical URL: ' + url)
        built = (dist / (path.lstrip('/') or 'index.html')).read_bytes()
        alternates = rb'<link rel="alternate" hreflang="[^"]+" href="[^"]+">'
        if set(re.findall(alternates, built)) != set(re.findall(alternates, body)):
            raise RuntimeError('Language alternates differ from build: ' + url)

    for path, markers in {
        '/home.html': (rb'<meta http-equiv="refresh"[^>]*>', rb'<link rel="canonical"[^>]*>'),
        '/robots.txt': (rb'(?m)^(?:User-agent|Allow|Disallow|Sitemap): [^\r\n]*',),
    }.items():
        built = (dist / path[1:]).read_bytes()
        deployed = fetch(base_url + path)
        if any(re.findall(pattern, built) != re.findall(pattern, deployed) for pattern in markers):
            raise RuntimeError('Search directives differ from build: ' + path)
    print(f'PASS: {len(expected)} sitemap URLs match the build; checked canonical URLs, legacy home and robots directives')


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
