from PIL import Image

from dev.Color import Color
from dev.view import View
from dev.AxisAlignment import AxisAlignment

class Column(View):
    def __init__(
            self,
            width: int,
            height: int,
            background: Color = Color(0, 0, 0, 0),
            children: list[View] = [],
            main_axis_alignment = AxisAlignment.start
        ):
        super().__init__(width, height, background=background)
        self.__children = children
        self.__coordinate: int = 0
        self.__main_axis_alignment = main_axis_alignment

    def generate(self) -> Image:
        children_image = [i.generate() for i in self.__children]
        background = self._make_background()
        y_coordinates = self.__main_axis_alignment.value.make(self._height, [i.get_height() for i in self.__children])
        for i in range(len(children_image)):
            background.paste(children_image[i], (0, y_coordinates[i]))

        return background
