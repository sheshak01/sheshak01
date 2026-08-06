from PIL import Image
import cv2
import numpy as np
from rembg import remove
import io


def process_image(image_path, width=90):
    # ----------------------------
    # Remove Background
    # ----------------------------
    with open(image_path, "rb") as f:
        input_data = f.read()

    output_data = remove(input_data)

    img = Image.open(io.BytesIO(output_data)).convert("RGBA")

    # White background
    background = Image.new("RGBA", img.size, (255, 255, 255, 255))
    img = Image.alpha_composite(background, img).convert("RGB")

    # ----------------------------
    # Convert to grayscale
    # ----------------------------
    gray = img.convert("L")

    img_np = np.array(gray)

    # ----------------------------
    # CLAHE Contrast Enhancement
    # ----------------------------
    clahe = cv2.createCLAHE(
        clipLimit=3.0,
        tileGridSize=(8, 8)
    )

    contrast = clahe.apply(img_np)

    # ----------------------------
    # Gamma Correction
    # ----------------------------
    gamma = 1.5

    corrected = np.array(
        255 * ((contrast / 255) ** gamma),
        dtype=np.uint8
    )

    # ----------------------------
    # Resize
    # ----------------------------
    h, w = corrected.shape

    rows = int(width * (h / w) * 0.48)

    resized = cv2.resize(
        corrected,
        (width, rows),
        interpolation=cv2.INTER_AREA
    )

    return resized