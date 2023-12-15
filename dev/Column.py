from PIL import Image

from dev.CrossAxisAlignment import CrossAxisAlignment
from dev.MainAxisAlignment import MainAxisAlignment
from dev.Color import Color
from dev.padding import Padding
from dev.view import View


class Column(View):
    def __init__(
            self,
            width: int,
            height: int,
            background: Color = Color(0, 0, 0, 0),
            children: list[View] = None,
            padding=Padding.all(0),
            main_axis_alignment=MainAxisAlignment.start,
            cross_axis_alignment=CrossAxisAlignment.center,
    ):
        super().__init__(width, height, background=background, padding=padding)
        if children is None:
            children = []
        self.__children = children
        self.__coordinate: int = 0
        self.__main_axis_alignment = main_axis_alignment
        self.__cross_axis_alignment = cross_axis_alignment

    def generate(self) -> Image:
        children_image = [i.generate() for i in self.__children]
        background = self._make_background()
        x_coordinates = self.__cross_axis_alignment.value.make(self._width, [i.get_width() for i in self.__children])
        y_coordinates = self.__main_axis_alignment.value.make(self._height, [i.get_height() for i in self.__children])
        for i in range(len(children_image)):
            background.paste(children_image[i], (x_coordinates[i], y_coordinates[i]))

        return background
