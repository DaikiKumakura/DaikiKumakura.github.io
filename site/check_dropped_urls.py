"""Warn before deploying when a live article URL would disappear (and then return 404).

Rescheduling or unpublishing an article that search engines already know turns its URL
into a 404 until it is published again. This compares the deployed sitemap with the one
just built and prints a GitHub Actions warning for every article URL that would vanish.
It never fails the build: hiding an article can be deliberate."""
import argparse
from pathlib import Path
from urllib.parse import urlsplit

from verify_deployment import fetch, locations


def articles(urls):
    return {url for url in urls if urlsplit(url).path.startswith('/writing/')}


def dropped(live_urls, built_urls):
    """Article URLs listed on the live site but absent from the new build."""
    return sorted(articles(live_urls) - set(built_urls))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dist', type=Path, default=Path(__file__).resolve().parent / 'dist')
    parser.add_argument('--base-url', default='https://daikikumakura.github.io')
    args = parser.parse_args()
    built = locations((args.dist / 'sitemap.xml').read_bytes())
    try:
        live = locations(fetch(args.base_url.rstrip('/') + '/sitemap.xml'))
    except Exception as error:  # noqa: BLE001 - advisory check only
        print(f'::notice title=Dropped-URL check skipped::live sitemap not readable: {error}')
        return
    gone = dropped(live, built)
    for url in gone:
        print(f'::warning title=Published article would return 404::{url} is live but missing from this build')
    print(f'{len(gone)} live article URL(s) would disappear' if gone else 'No live article URL disappears in this build')


if __name__ == '__main__':
    main()
