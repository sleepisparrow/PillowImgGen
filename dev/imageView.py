import requests
from PIL import Image

from dev.Color import Color
from dev.alignment import Alignment
from dev.imageOption import ImageOption
from dev.padding import Padding
from dev.view import View


class ImageView(View):
    def __init__(
            self,
            width: int = None,
            height: int = None,
            path: str = None,
            background: Color = Color(0, 0, 0, 0),
            child: View = None,
            alignment: Alignment = Alignment.top_left,
            padding: Padding = Padding.all(0),
            image_option = ImageOption.fill,
    ):
        # 1. width height 둘 중 하나만 있는 경우 에러
        if (width is None) != (height is None):
            raise ValueError("If you give width or height, you must give other one too.")
        # 2. 모두 없는 경우
        if width is None and height is None and path is None:
            raise ValueError("You must give path or width and height.")

        if not isinstance(image_option, ImageOption):
            raise TypeError("image_option must be enum of ImageOption")

        self.imageOption = image_option

        image: Image = None
        if path is not None:
            image: Image = self.__get_image(path)

        if width is None and height is None:
            size = image.size or [0, 0]
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
        background = self._make_background()
        foreground = self._make_aligned_child()
        self.__make_image()
        if self.__image is not None:
            background.paste(self.__image)
        if foreground is not None:
            background.paste(foreground, mask=foreground)
        return background

    # 배경 -> 사진 -> 자식 순서로 진행되어야 함.

    def __make_image(self):
        """
        이미지를 옵션에 따라 크롭하거나 크기를 변경하는 함수
        OCP를 만족하지 않음...
        :return:
        """

        if self.__image is None:
            return
        if self.imageOption == ImageOption.fill:
            self.__image = self.__image.resize((self._width, self._height))
        elif self.imageOption == ImageOption.crop:
            self.__image = self.__image.crop((0, 0, self._width, self._height))
