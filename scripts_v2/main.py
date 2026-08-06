from preprocess import preprocess
from ascii_converter import image_to_ascii

from PIL import Image
import os

INPUT_IMAGE = "assets/profile.png"
OUTPUT_DIR = "generated"

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=" * 50)
print("GitHub ASCII Portrait Generator V2")
print("=" * 50)

print("\n[1/3] Preprocessing image...")

processed = preprocess(INPUT_IMAGE)

processed_path = os.path.join(
    OUTPUT_DIR,
    "processed_v2.png"
)

Image.fromarray(processed).save(processed_path)

print("✓ Saved:", processed_path)

print("\n[2/3] Generating ASCII portrait...")

ascii_art = image_to_ascii(
    processed,
    width=140
)

portrait_path = os.path.join(
    OUTPUT_DIR,
    "portrait_v2.txt"
)

with open(
    portrait_path,
    "w",
    encoding="utf-8"
) as f:

    for line in ascii_art:
        f.write(line + "\n")

print("✓ Saved:", portrait_path)

print("\n[3/3] Preview\n")

for line in ascii_art[:20]:
    print(line)

print("\n" + "=" * 50)
print("Generation Complete")
print("=" * 50)