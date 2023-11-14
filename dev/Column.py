from PIL import Image

from dev.Color import Color
from dev.view import View


class Column(View):
    def __init__(
            self,
            width: int,
            height: int,
            background: Color = Color(0, 0, 0, 0),
            children: list[View] = [], ):
        super().__init__(width, height, background=background)
        self.children = children
        self.__coordinate: int = 0

    def generate(self) -> Image:
        children_image = [i.generate() for i in self.children]
        background = self._make_background()
        for image in children_image:
            background.paste(image, (0, self.__coordinate))
            self.__coordinate += image.size[1]

        return background
