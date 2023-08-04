from typing import Tuple

from PIL import Image


def generate_image(width: int, height: int):
    if width <= 0 or height <= 0:
        raise ValueError(f"width, height must be positive value: (width: {width}, height: {height})")
    return Image.new(mode="RGBA", size=(width, height), color=(255, 255, 255, 0))


class View:
    def __init__(self, width: int, height: int, background_rgba: Tuple[int, int, int, int] = (0, 0, 0, 0)):
        """
        :param width: width of this view
        :param height: height of view
        :type background_rgba: tuple for background rgba
        """

        self.background_rgba = background_rgba
        self.width = width
        self.height = height

    def generate(self):
        return Image.new(mode="RGBA", size=(self.width, self.height), color=self.background_rgba)
