import warnings

from PIL import Image

from dev.Color import Color
from dev.alignment import Alignment
from dev.padding import Padding


class View:
    def __init__(
        self,
        width: int,
        height: int,
        background: Color = Color(0, 0, 0, 0),
        child=None,
        alignment=Alignment.top_left,
        padding=Padding.all(0)
    ):
        """
        :param width: width of this view
        :param height: height of view
        :param background: tuple for background rgba
        :type child: View
        :param child: child of this view. it must not overflow parent's section
        :param alignment: the way to alignment child.
        :param padding: padding of itself.
        """
        if not isinstance(child, View) and child is not None:
            raise TypeError(
                f"child must be subclass of View but you gave {type(child)}")

        if alignment is None:
            alignment = Alignment.top_left
        if not isinstance(alignment, Alignment):
            raise TypeError(
                f"alignment must be enum of Alignment but you gave {type(alignment)}")

        if type(padding) != Padding:
            raise TypeError(
                f"padding must be instance of Padding. but you gave {type(padding)}")

        self.__child = child
        self.__background = background
        self.__width = width
        self.__height = height
        self.__alignment = alignment
        self.__padding = padding
        
        if child is not None:
            child_padding = child.get_padding()
            self.__padding_view_width = width - child_padding.get_horizontal_padding()
            self.__padding_view_height = width - child_padding.get_vertical_padding()

    def get_padding(self):
        return self.__padding

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
        box = [0, 0,]
        child_width = self.__child.get_width()
        child_height = self.__child.get_height()
        # box 구하기
        alignment_value = self.__alignment.value
        if alignment_value % 3 == 0:
            box[0] = 0
        elif alignment_value % 3 == 1:
            box[0] = (self.__padding_view_width - child_width) // 2
        else:
            box[0] = self.__padding_view_width - child_width
        # box[2] = box[0] + child_width

        if alignment_value // 3 == 0:
            box[1] = 0
        elif alignment_value // 3 == 1:
            box[1] = (self.__padding_view_height - child_height) // 2
        else:
            box[1] = self.__padding_view_height - child_height
        # box[3] = box[1] + child_height

        return tuple(box)

    def _warn_if_child_is_bigger_than_padding_view(self):
        """
        print warning if child is bigger than padding.
        :return: nothing
        """
        p_height = self.__padding_view_height
        p_width = self.__padding_view_width

        c_height = self.__child.get_height()
        c_width = self.__child.get_width()

        if p_height < c_height or p_width < c_width:
            warnings.warn("Child's size is bigger than parent", Warning)

    def generate(self) -> Image:
        """
        generate image file based on attribute of this object
        :return: an Image.
        """
        parent = Image.new(mode="RGBA", size=(
            self.__width, self.__height), color=self.__background.get_RGBA_by_tuple())
        if self.__child is not None:
            child_img = self.__child.generate()
            child_padding = self.__child.get_padding()
            virtual_view_for_padding = Image.new("RGBA", (self.__padding_view_width, self.__padding_view_height), color=(0, 0, 0, 0))
            # TODO: 아래 메서드 두개 고치기
            self._warn_if_child_is_bigger_than_padding_view()
            virtual_view_for_padding.paste(child_img, self._get_alignment(), child_img)
            
            parent.paste(virtual_view_for_padding, box=(child_padding.left, child_padding.top), mask=virtual_view_for_padding)

        return parent
