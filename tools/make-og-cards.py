#!/usr/bin/env python3
"""Regenerate the link-preview cards in assets/og-de.jpg and assets/og-en.jpg.

These are what WhatsApp, Signal, Facebook and LinkedIn show when someone
shares a link. They repeat the homepage hero as type on the dark ground, one
card per language, at the 1200x630 Open Graph size.

    python3 tools/make-og-cards.py

Requires macOS: it renders through qlmanage and resizes with sips. The fonts
are fetched from Google Fonts (Spectral and IBM Plex, both OFL) and embedded
in the SVG, so the card uses the same faces as the site rather than whatever
happens to be installed.

Edit CARDS below when the tagline changes, then rerun and commit the JPEGs.
"""

import base64, os, re, shutil, struct, subprocess, sys, tempfile, urllib.request, zlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FACES = [  # family, style, weight, Google Fonts query fragment
    ("Spectral", "normal", "500", "Spectral:wght@500"),
    ("Spectral", "normal", "300", "Spectral:wght@300"),
    ("Spectral", "italic", "300", "Spectral:ital,wght@1,300"),
    ("PlexMono", "normal", "500", "IBM+Plex+Mono:wght@500"),
    ("PlexSans", "normal", "500", "IBM+Plex+Sans:wght@500"),
]

CARDS = {
    "de": dict(eyebrow="VEREIN · SOLOTHURN · SEIT 2012",
               tagline="Verein zur Erhaltung und Förderung",
               tagline2="von geistbewegendem Wissen",
               cta="Hilf mit, geistbewegendes Wissen zu bewahren."),
    "en": dict(eyebrow="ASSOCIATION · SOLOTHURN · SINCE 2012",
               tagline="Association for the preservation and",
               tagline2="promotion of mind-moving knowledge",
               cta="Help preserve mind-moving knowledge."),
}

# Coordinates are in 1200x630 space via the viewBox. The SVG is declared
# 768 wide because that is the viewport qlmanage renders into - anything
# past it would be cropped away.
TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="768" height="403" viewBox="0 0 1200 630">
<defs><style>{fonts}</style></defs>
<rect width="1200" height="630" fill="#0E1A18"/>
<rect x="84" y="112" width="42" height="1.5" fill="#D9B872"/>
<text x="142" y="118" font-family="PlexMono" font-weight="500" font-size="19"
      letter-spacing="4.2" fill="#D9B872">{eyebrow}</text>
<text x="84" y="258" font-family="Spectral" font-weight="500" font-size="96"
      letter-spacing="-1.4" fill="#F5F0E6">Bibliotheca</text>
<text x="84" y="356" font-family="Spectral" font-weight="300" font-size="96"
      letter-spacing="0.5" fill="#D9B872">Psychonautica</text>
<text x="84" y="424" font-family="Spectral" font-style="italic" font-weight="300"
      font-size="30" fill="#D8D4C7">{tagline}</text>
<text x="84" y="462" font-family="Spectral" font-style="italic" font-weight="300"
      font-size="30" fill="#D8D4C7">{tagline2}</text>
<rect x="84" y="506" width="440" height="1" fill="#D9B872" fill-opacity="0.30"/>
<text x="84" y="560" font-family="PlexSans" font-weight="500" font-size="27"
      fill="#F5F0E6">{cta}</text>
</svg>"""

RENDER_PX = 2400                      # qlmanage renders square; the card lands top-left
CARD_ROWS = round(RENDER_PX * 403 / 768)


def fetch_fonts(workdir):
    """Download each face and return it as an embeddable @font-face block."""
    blocks = []
    for family, style, weight, query in FACES:
        css = urllib.request.urlopen(urllib.request.Request(
            f"https://fonts.googleapis.com/css2?family={query}&display=swap",
            headers={"User-Agent": "Mozilla/5.0"})).read().decode()
        url = re.search(r"url\((https://[^)]+)\)", css).group(1)
        data = urllib.request.urlopen(url).read()
        blocks.append(f"@font-face{{font-family:'{family}';font-style:{style};"
                      f"font-weight:{weight};src:url(data:font/ttf;base64,"
                      f"{base64.b64encode(data).decode()}) format('truetype')}}")
        print(f"  fetched {family} {style} {weight}")
    return "".join(blocks)


def png_rows(path):
    """Decode a PNG to a list of unfiltered scanlines."""
    data = open(path, "rb").read()
    pos, idat = 8, b""
    while pos < len(data):
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        kind = data[pos + 4:pos + 8]
        if kind == b"IHDR":
            w, h, _, colour = struct.unpack(">IIBB", data[pos + 8:pos + 18])
        elif kind == b"IDAT":
            idat += data[pos + 8:pos + 8 + length]
        pos += 12 + length
    raw = zlib.decompress(idat)
    channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[colour]
    stride, prev, rows, i = w * channels, bytearray(w * channels), [], 0
    for _ in range(h):
        filt, i = raw[i], i + 1
        line, i = bytearray(raw[i:i + stride]), i + stride
        for x in range(stride):
            a = line[x - channels] if x >= channels else 0
            b = prev[x]
            c = prev[x - channels] if x >= channels else 0
            if filt == 1: line[x] = (line[x] + a) & 255
            elif filt == 2: line[x] = (line[x] + b) & 255
            elif filt == 3: line[x] = (line[x] + (a + b) // 2) & 255
            elif filt == 4:
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                line[x] = (line[x] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        rows.append(bytes(line)); prev = line
    return w, channels, rows


def write_png(path, width, rows, channels):
    raw = b"".join(b"\x00" + row for row in rows)
    def chunk(kind, payload):
        return (struct.pack(">I", len(payload)) + kind + payload
                + struct.pack(">I", zlib.crc32(kind + payload) & 0xffffffff))
    colour = {1: 0, 2: 4, 3: 2, 4: 6}[channels]
    open(path, "wb").write(
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", width, len(rows), 8, colour, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw, 9))
        + chunk(b"IEND", b""))


def main():
    if not shutil.which("qlmanage") or not shutil.which("sips"):
        sys.exit("This script needs macOS (qlmanage and sips).")
    work = tempfile.mkdtemp(prefix="og-cards-")
    fonts = fetch_fonts(work)
    for lang, text in CARDS.items():
        svg = os.path.join(work, f"card-{lang}.svg")
        open(svg, "w", encoding="utf-8").write(TEMPLATE.format(fonts=fonts, **text))
        subprocess.run(["qlmanage", "-t", "-s", str(RENDER_PX), "-o", work, svg],
                       capture_output=True)
        rendered = svg + ".png"
        width, channels, rows = png_rows(rendered)
        cropped = os.path.join(work, f"top-{lang}.png")
        write_png(cropped, width, rows[:CARD_ROWS], channels)
        out = os.path.join(ROOT, "assets", f"og-{lang}.jpg")
        subprocess.run(["sips", "-z", "630", "1200", "-s", "format", "jpeg",
                        "-s", "formatOptions", "88", cropped, "--out", out],
                       capture_output=True)
        print(f"  wrote assets/og-{lang}.jpg ({os.path.getsize(out) // 1024} KB)")
    shutil.rmtree(work, ignore_errors=True)
    print("\nRemember to rerun: python3 tools/i18n/i18n.py build")


if __name__ == "__main__":
    main()
