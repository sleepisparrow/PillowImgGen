from typing import Tuple

from PIL import Image


def generate_image(width: int, height: int):
    if width <= 0 or height <= 0:
        raise ValueError(f"width, height must be positive value: (width: {width}, height: {height})")
    return Image.new(mode="RGBA", size=(width, height), color=(255, 255, 255, 0))
