import warnings

from PIL import Image

from dev.Color import Color
from dev.alignment import Alignment


class View:
    def __init__(self,
                 width: int,
                 height: int,
                 background: Color = Color(0, 0, 0, 0),
                 child=None,
                 alignment=Alignment.top_left):
        """
        :param width: width of this view
        :param height: height of view
        :param background: tuple for background rgba
        :type child: View
        :param child: child of this view. it must not overflow parent's section
        """
        if not isinstance(child, View) and child is not None:
            raise TypeError(f"child must be subclass of View but you give {type(child)}")

        if alignment is None:
            alignment = Alignment.top_left

        self.__child = child
        self.__background = background
        self.__width = width
        self.__height = height
        self.__alignment = alignment

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def _get_h_center(self) -> int:
        """
        :return: x value of horizontal center
        """
        return (self.__width - self.__child.get_width()) // 2

    def _get_v_center(self):
        """
        :return: y value of vertical center
        """
        return (self.__height - self.__child.get_height()) // 2

    def _get_alignment(self) -> tuple:
        """
        calculate position of child by alignment.
        :return: position of child.
        """
        box = [0, 0]
        # box 구하기
        alignment_value = self.__alignment.value
        if alignment_value % 3 == 0:
            box[0] = 0
        elif alignment_value % 3 == 1:
            box[0] = (self.__width - self.__child.get_width()) // 2
        else:
            box[0] = self.__width - self.__child.get_width()

        if alignment_value // 3 == 0:
            box[1] = 0
        elif alignment_value // 3 == 1:
            pass  # TODO
        else:
            pass  # TODO
        return tuple(box)

    def _warn_if_child_is_bigger_than_parent(self):
        """
        print warning if child is bigger than child.
        :return: nothing
        """
        p_height = self.__height
        p_width = self.__width

        c_height = self.__child.get_height()
        c_width = self.__child.get_width()

        if p_height < c_height or p_width < c_width:
            warnings.warn("Child's size is bigger than parent", Warning)

    def generate(self) -> Image:
        """
        generate image file based on attribute of this object
        :return: an Image.
        """
        parent = Image.new(mode="RGBA", size=(self.__width, self.__height), color=self.__background.get_RGBA_by_tuple())
        if self.__child is not None:
            child = self.__child.generate()
            self._warn_if_child_is_bigger_than_parent()
            parent.paste(child, self._get_alignment())

        return parent
