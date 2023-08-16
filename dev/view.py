from PIL import Image

from dev.Color import Color


class View:
    def __init__(self, width: int, height: int, background: Color = Color(0, 0, 0, 0)):
        """
        :param width: width of this view
        :param height: height of view
        :type background: tuple for background rgba
        """

        self.background = background
        self.width = width
        self.height = height

    def generate(self):
        return Image.new(mode="RGBA", size=(self.width, self.height), color=self.background.get_RGBA_by_tuple())

