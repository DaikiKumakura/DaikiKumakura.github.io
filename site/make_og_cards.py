"""Make 1200x630 social-preview cards (LinkedIn, X, Slack) by hand; the build only copies them.

    python site/make_og_cards.py --default      site-wide card: assets/og-default.png
    python site/make_og_cards.py --live         cards for every published article
    python site/make_og_cards.py slug [slug...] cards for the named articles

An article card is the article's first figure fitted onto a white 1200x630 canvas,
saved as content/articles/<slug>/og.png. The build publishes it as writing/og/<slug>.png
only when the article itself is published. Needs Pillow; an SVG figure is rendered
with Microsoft Edge (headless). This is not a build dependency.
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit('Pillow is required: python -m pip install pillow')

BASE = Path(__file__).resolve().parent
SIZE = (1200, 630)
ACCENT, INK, MUTED, WHITE = (37, 87, 123), (37, 37, 37), (89, 89, 89), (255, 255, 255)
FONT_BOLD = [r'C:\Windows\Fonts\YuGothB.ttc', r'C:\Windows\Fonts\meiryob.ttc', r'C:\Windows\Fonts\segoeuib.ttf']
FONT_REGULAR = [r'C:\Windows\Fonts\YuGothM.ttc', r'C:\Windows\Fonts\meiryo.ttc', r'C:\Windows\Fonts\segoeui.ttf']
EDGE = [r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe', r'C:\Program Files\Microsoft\Edge\Application\msedge.exe']


def font(candidates, size):
    for path in candidates:
        if Path(path).is_file():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def default_card(out):
    image = Image.new('RGB', SIZE, WHITE)
    draw = ImageDraw.Draw(image)
    draw.rectangle([0, 0, 24, SIZE[1]], fill=ACCENT)
    draw.text((90, 150), 'Daiki Kumakura', font=font(FONT_BOLD, 96), fill=INK)
    draw.text((94, 280), '熊倉大騎', font=font(FONT_REGULAR, 46), fill=MUTED)
    draw.text((92, 380), 'Mathematical biology and PK/PD modeling', font=font(FONT_BOLD, 44), fill=ACCENT)
    draw.text((92, 450), 'Public-data analyses of dosing, exposure and uncertainty', font=font(FONT_REGULAR, 32), fill=MUTED)
    draw.text((92, 550), 'daikikumakura.github.io', font=font(FONT_REGULAR, 28), fill=MUTED)
    image.save(out, optimize=True)
    print('wrote', out)


def svg_size(path):
    head = path.read_text(encoding='utf-8', errors='ignore')[:4000]
    root = re.search(r'<svg\b[^>]*>', head)[0]
    w, h = (re.search(rf'\s{k}="([\d.]+)', root) for k in ('width', 'height'))
    if w and h:
        return float(w[1]), float(h[1])
    box = re.search(r'viewBox="[\d.\-]+[ ,]+[\d.\-]+[ ,]+([\d.]+)[ ,]+([\d.]+)"', root)
    return float(box[1]), float(box[2])


def render_svg(svg, out):
    edge = next((p for p in EDGE if Path(p).is_file()), None)
    if not edge:
        raise SystemExit(f'Microsoft Edge is needed to render {svg.name}')
    w, h = (round(v * 2) for v in svg_size(svg))
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        page = Path(tmp) / 'page.html'
        page.write_text(f'<html><body style="margin:0;background:#fff"><img src="{svg.as_uri()}" style="width:{w}px;height:{h}px;display:block"></body></html>', encoding='utf-8')
        subprocess.run([edge, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run', f'--user-data-dir={Path(tmp) / "profile"}',
                        f'--window-size={w},{h}', f'--screenshot={out}', page.as_uri()],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
        # Edge may hand the work to another process and return first: wait for the file.
        for _ in range(60):
            if Path(out).is_file() and Path(out).stat().st_size > 0:
                time.sleep(0.5)
                return
            time.sleep(0.5)
        raise SystemExit(f'Edge did not produce a screenshot of {svg.name}')


def first_figure(folder, slug):
    meta = json.loads((folder / 'meta.json').read_text(encoding='utf-8'))
    text = (folder / f"{meta['source_language']}.md").read_text(encoding='utf-8')
    prefix = f'shared/{slug}/'
    for match in re.finditer(r'!\[[^\]]*\]\(([^)\s]+)\)|<img[^>]+src="([^"]+)"', text):
        ref = match.group(1) or match.group(2)
        if ref.startswith(prefix):
            path = folder / 'shared' / ref[len(prefix):]
            if path.suffix.lower() in ('.png', '.jpg', '.jpeg', '.svg') and path.is_file():
                return path
    return None


def article_card(folder):
    slug = folder.name
    figure = first_figure(folder, slug)
    if figure is None:
        print('skip (no figure):', slug)
        return
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        source = figure
        if figure.suffix.lower() == '.svg':
            source = Path(tmp) / 'figure.png'
            render_svg(figure, source)
        art = Image.open(source).convert('RGBA')
        background = Image.new('RGBA', art.size, WHITE + (255,))
        art = Image.alpha_composite(background, art).convert('RGB')
        canvas = Image.new('RGB', SIZE, WHITE)
        draw = ImageDraw.Draw(canvas)
        draw.rectangle([0, 0, SIZE[0], 8], fill=ACCENT)
        box_w, box_h = 1100, 500
        scale = min(box_w / art.width, box_h / art.height)
        art = art.resize((max(1, round(art.width * scale)), max(1, round(art.height * scale))), Image.LANCZOS)
        canvas.paste(art, ((SIZE[0] - art.width) // 2, 28 + (box_h - art.height) // 2))
        draw.text((50, 570), 'Daiki Kumakura', font=font(FONT_BOLD, 26), fill=ACCENT)
        label = 'daikikumakura.github.io'
        right = font(FONT_REGULAR, 24)
        draw.text((SIZE[0] - 50 - draw.textlength(label, font=right), 572), label, font=right, fill=MUTED)
        out = folder / 'og.png'
        canvas.save(out, optimize=True)
        print('wrote', out.relative_to(BASE.parent), f'({out.stat().st_size // 1024} KB, from {figure.name})')


def live_slugs():
    now = datetime.now(timezone.utc)
    slugs = []
    for meta_path in sorted((BASE / 'content/articles').glob('*/meta.json')):
        meta = json.loads(meta_path.read_text(encoding='utf-8'))
        publish_at = meta.get('publish_at')
        if not meta['draft'] and not (publish_at and now < datetime.fromisoformat(publish_at)):
            slugs.append(meta_path.parent.name)
    return slugs


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('slugs', nargs='*')
    parser.add_argument('--default', action='store_true')
    parser.add_argument('--live', action='store_true')
    args = parser.parse_args()
    if not (args.default or args.live or args.slugs):
        parser.error('name an article, or use --default or --live')
    if args.default:
        default_card(BASE / 'assets/og-default.png')
    for slug in (live_slugs() if args.live else []) + args.slugs:
        article_card(BASE / 'content/articles' / slug)


if __name__ == '__main__':
    main()
