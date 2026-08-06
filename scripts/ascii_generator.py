# ==========================================
# ASCII Character Set
# Dark -> Light
# ==========================================

ASCII_CHARS = "@%#*+=-:. "


def generate_ascii(image):
    ascii_art = []

    levels = len(ASCII_CHARS) - 1

    for row in image:

        line = ""

        for pixel in row:

            # Invert brightness so dark pixels become '@'
            index = int((255 - pixel) / 255 * levels)

            line += ASCII_CHARS[index]

        ascii_art.append(line)

    return ascii_art