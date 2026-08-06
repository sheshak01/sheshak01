from PIL import Image, ImageOps
from rembg import remove
import cv2
import numpy as np
import io


def preprocess(image_path):
    # Read image
    with open(image_path, "rb") as f:
        input_data = f.read()

    # Remove background
    output = remove(input_data)

    img = Image.open(io.BytesIO(output)).convert("RGBA")

    # Composite onto white background
    bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
    img = Image.alpha_composite(bg, img).convert("RGB")

    # Crop to non-white content
    bbox = ImageOps.invert(img.convert("L")).getbbox()
    if bbox:
        img = img.crop(bbox)

    # Convert to OpenCV
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # Resize
    img = cv2.resize(img, (450, 450))

    # Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
    gray = clahe.apply(gray)

    # Mild sharpening
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    gray = cv2.filter2D(gray, -1, kernel)

    return gray