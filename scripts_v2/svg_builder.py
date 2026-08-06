from pathlib import Path

INPUT_FILE = "generated/portrait_v2.txt"
OUTPUT_FILE = "generated/portrait_v2.svg"

FONT_SIZE = 9
LINE_HEIGHT = 11
CHAR_WIDTH = 6
MARGIN = 20


def escape_xml(text):
    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
    )


with open(INPUT_FILE, "r", encoding="utf-8") as f:
    lines = [line.rstrip("\n") for line in f]

max_width = max(len(line) for line in lines)

svg_width = max_width * CHAR_WIDTH + MARGIN * 2
svg_height = len(lines) * LINE_HEIGHT + MARGIN * 2

svg = []

svg.append('<?xml version="1.0" encoding="UTF-8"?>')

svg.append(
    f'<svg xmlns="http://www.w3.org/2000/svg" '
    f'width="{svg_width}" '
    f'height="{svg_height}" '
    f'viewBox="0 0 {svg_width} {svg_height}">'
)

svg.append('<rect width="100%" height="100%" fill="white"/>')

svg.append(
    '<text '
    f'font-family="monospace" '
    f'font-size="{FONT_SIZE}" '
    'fill="black">'
)

delay = 0.0

for i, line in enumerate(lines):

    y = MARGIN + (i + 1) * LINE_HEIGHT

    svg.append(
        f'''
<tspan
x="{MARGIN}"
y="{y}"
opacity="0">
{escape_xml(line)}
<animate
attributeName="opacity"
from="0"
to="1"
begin="{delay:.2f}s"
dur="0.15s"
fill="freeze"/>
</tspan>
'''
    )

    delay += 0.05

svg.append("</text>")
svg.append("</svg>")

Path(OUTPUT_FILE).write_text(
    "\n".join(svg),
    encoding="utf-8"
)

print("Animated SVG Generated!")