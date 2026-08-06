import cv2

# Simple high-contrast ASCII ramp
ASCII_CHARS = "@%#*+=-:. "


def image_to_ascii(image, width=140):
    """
    Convert grayscale image to ASCII art.
    """

    h, w = image.shape

    aspect_ratio = h / w

    # Character height is roughly twice the width
    height = int(width * aspect_ratio * 0.5)

    resized = cv2.resize(
        image,
        (width, height),
        interpolation=cv2.INTER_AREA
    )

    ascii_art = []

    scale = len(ASCII_CHARS) - 1

    for row in resized:

        line = ""

        for pixel in row:

            # Map pixel (0-255) to character index
            index = int((255 - pixel) * scale / 255)

            line += ASCII_CHARS[index]

        ascii_art.append(line)

    return ascii_art