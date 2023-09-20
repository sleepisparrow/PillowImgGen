import requests
from PIL import Image

from dev.Color import Color
from dev.alignment import Alignment
from dev.padding import Padding
from dev.view import View


class ImageView(View):
    def __init__(
            self,
            width: int = None,
            height: int = None,
            image: str = None,
            background: Color = Color(0, 0, 0, 0),
            child: View = None,
            alignment: Alignment = Alignment.top_left,
            padding: Padding = Padding.all(0),
    ):
        if image is None and (width is None or height is None):
            # TODO TypeError 제대로 쓰기
            raise TypeError("부족한 인수!")

        if image is not None and (width is not None or height is not None):
            # TODO 잘못된 인수 TypeError
            raise TypeError("부족한 인수!")

        if image is not None:
            image: Image = self.__get_image(image)

        if width is None and height is None:
            size = image.size
            width = size[0]
            height = size[1]

        super().__init__(width, height, background, child, alignment, padding)
        self.__image = image

    @staticmethod
    def __get_image(path) -> Image:
        try:
            return Image.open(requests.get(path, stream=True).raw)
        except requests.exceptions.MissingSchema:
            return Image.open(path)

    def generate(self) -> Image:
        background = super().generate()
        background.paste(self.__image)
        return background
