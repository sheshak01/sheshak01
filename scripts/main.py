from image_processor import process_image
from ascii_generator import generate_ascii
from PIL import Image
import os

# ======================================
# Configuration
# ======================================

IMAGE_PATH = "assets/profile.png"
OUTPUT_DIR = "generated"

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Processing image...")

# ======================================
# Process Image
# ======================================

processed_image = process_image(IMAGE_PATH)

# Save processed image for inspection
Image.fromarray(processed_image).save(
    os.path.join(OUTPUT_DIR, "processed.png")
)

print("Generating ASCII...")

# ======================================
# Generate ASCII
# ======================================

ascii_art = generate_ascii(processed_image)

# ======================================
# Save ASCII
# ======================================

output_file = os.path.join(
    OUTPUT_DIR,
    "portrait.txt"
)

with open(
    output_file,
    "w",
    encoding="utf-8"
) as f:

    for line in ascii_art:
        f.write(line + "\n")

print("ASCII portrait generated successfully!")

print(f"Saved to: {output_file}")

print("Processed image saved to generated/processed.png")

print("\nPreview:\n")

for line in ascii_art[:15]:
    print(line)