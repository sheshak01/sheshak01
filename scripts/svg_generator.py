from pathlib import Path

INPUT_FILE = "generated/portrait.txt"
OUTPUT_FILE = "generated/portrait.svg"

FONT_SIZE = 12
CHAR_WIDTH = 7.2
LINE_HEIGHT = 15

# Read ASCII art
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    lines = [line.rstrip("\n") for line in f]

width = max(len(line) for line in lines) * CHAR_WIDTH
height = len(lines) * LINE_HEIGHT

svg = []

svg.append(
    f'<svg xmlns="http://www.w3.org/2000/svg" '
    f'width="{width}" height="{height}" '
    f'viewBox="0 0 {width} {height}">'
)

svg.append(
    '<rect width="100%" height="100%" fill="white"/>'
)

svg.append(
    f'<text font-family="monospace" '
    f'font-size="{FONT_SIZE}" '
    f'fill="black">'
)

for i, line in enumerate(lines):
    y = (i + 1) * LINE_HEIGHT

    svg.append(
        f'<tspan x="0" y="{y}">{line}</tspan>'
    )

svg.append("</text>")
svg.append("</svg>")

Path(OUTPUT_FILE).write_text(
    "\n".join(svg),
    encoding="utf-8"
)

print("SVG generated successfully!")
print(f"Saved to: {OUTPUT_FILE}")