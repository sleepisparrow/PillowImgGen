import logging
import warnings

from PIL import Image

from dev.Color import Color


class View:
    def __init__(self,
                 width: int,
                 height: int,
                 background: Color = Color(0, 0, 0, 0),
                 child=None):
        """
        :param width: width of this view
        :param height: height of view
        :param background: tuple for background rgba
        :type child: View
        :param child: child of this view. it must not overflow parent's section
        """
        if not isinstance(child, View) and child is not None:
            raise TypeError(f"child must be subclass of View but you give {type(child)}")

        self.__child = child
        self.__background = background
        self.__width = width
        self.__height = height

    def generate(self):
        parent = Image.new(mode="RGBA", size=(self.__width, self.__height), color=self.__background.get_RGBA_by_tuple())
        if self.__child is not None:
            child = self.__child.generate()
            p_size = parent.size
            c_size = child.size

            if p_size[0] < c_size[0] or p_size[1] < c_size[1]:
                warnings.warn("Child's size is bigger than parent", Warning)
            parent.paste(child, (0, 0))

        return parent
