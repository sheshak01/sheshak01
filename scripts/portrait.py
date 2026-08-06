from PIL import Image
import cv2
import numpy as np
import os

# ==========================================
# CONFIGURATION
# ==========================================

IMAGE_PATH = "assets/profile.png"
OUTPUT_DIR = "generated"

ASCII_CHARS = " .`:-=+*cs#%@"

ASCII_WIDTH = 90

# ==========================================
# CREATE OUTPUT DIRECTORY
# ==========================================

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==========================================
# LOAD IMAGE
# ==========================================

print("Loading image...")

image = Image.open(IMAGE_PATH)

# ==========================================
# CONVERT TO GRAYSCALE
# ==========================================

gray = image.convert("L")
gray.save(f"{OUTPUT_DIR}/grayscale.png")

print("✓ Grayscale complete")

# ==========================================
# READ USING OPENCV
# ==========================================

img = cv2.imread(
    f"{OUTPUT_DIR}/grayscale.png",
    cv2.IMREAD_GRAYSCALE
)

# ==========================================
# CLAHE CONTRAST ENHANCEMENT
# ==========================================

clahe = cv2.createCLAHE(
    clipLimit=3.0,
    tileGridSize=(8, 8)
)

contrast = clahe.apply(img)

cv2.imwrite(
    f"{OUTPUT_DIR}/contrast.png",
    contrast
)

print("✓ Contrast enhanced")

# ==========================================
# DARKENING CURVE
# ==========================================

dark = ((contrast / 255.0) ** 1.7) * 255

dark = np.clip(
    dark,
    0,
    255
).astype(np.uint8)

cv2.imwrite(
    f"{OUTPUT_DIR}/darkened.png",
    dark
)

print("✓ Darkening applied")

# ==========================================
# RESIZE FOR ASCII
# ==========================================

height, width = dark.shape

ascii_height = int(
    ASCII_WIDTH * (height / width) * 0.48
)

resized = cv2.resize(
    dark,
    (ASCII_WIDTH, ascii_height),
    interpolation=cv2.INTER_AREA
)

cv2.imwrite(
    f"{OUTPUT_DIR}/resized.png",
    resized
)

print("✓ Image resized")

# ==========================================
# CONVERT TO ASCII
# ==========================================

levels = len(ASCII_CHARS) - 1

ascii_art = []

for row in resized:

    line = ""

    for pixel in row:

        brightness = pixel / 255.0

        index = int(brightness * levels)

        line += ASCII_CHARS[index]

    ascii_art.append(line)

# ==========================================
# SAVE ASCII
# ==========================================

with open(
    f"{OUTPUT_DIR}/portrait.txt",
    "w",
    encoding="utf-8"
) as f:

    for line in ascii_art:
        f.write(line + "\n")

print("✓ ASCII text generated")

# ==========================================
# PREVIEW
# ==========================================

print("\nPreview:\n")

for line in ascii_art[:15]:
    print(line)

print("\n")

# ==========================================
# SUMMARY
# ==========================================

print("=" * 50)
print("ASCII PORTRAIT GENERATED SUCCESSFULLY")
print("=" * 50)

print(f"Original Image : {width} x {height}")
print(f"ASCII Size     : {ASCII_WIDTH} x {ascii_height}")

print("\nGenerated Files")

print("generated/grayscale.png")
print("generated/contrast.png")
print("generated/darkened.png")
print("generated/resized.png")
print("generated/portrait.txt")

print("=" * 50)