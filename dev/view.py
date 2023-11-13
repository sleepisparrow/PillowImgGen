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

        if not isinstance(padding, Padding):
            raise TypeError(
                f"padding must be instance of Padding. but you gave {type(padding)}")

        self._child = child
        self._background = background
        self._width = width
        self._height = height
        self._alignment = alignment
        self._padding = padding

        if child is not None:
            child_padding = child.get_padding()
            self._padding_view_width = width - child_padding.get_horizontal_padding()
            self._padding_view_height = width - child_padding.get_vertical_padding()

    def get_padding(self):
        return self._padding

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def _get_h_center(self) -> int:
        """
        :return: x value of horizontal center
        """
        return (self._width - self._child.get_width()) // 2

    def _get_v_center(self):
        """
        :return: y value of vertical center
        """
        return (self._height - self._child.get_height()) // 2

    def _get_alignment(self) -> tuple:
        """
        calculate position of child by alignment.
        :return: position of child.
        """
        box = [0, 0, ]
        child_width = self._child.get_width()
        child_height = self._child.get_height()
        # box 구하기
        alignment_value = self._alignment.value
        if alignment_value % 3 == 0:
            box[0] = 0
        elif alignment_value % 3 == 1:
            box[0] = (self._padding_view_width - child_width) // 2
        else:
            box[0] = self._padding_view_width - child_width
        # box[2] = box[0] + child_width

        if alignment_value // 3 == 0:
            box[1] = 0
        elif alignment_value // 3 == 1:
            box[1] = (self._padding_view_height - child_height) // 2
        else:
            box[1] = self._padding_view_height - child_height
        # box[3] = box[1] + child_height

        return tuple(box)

    def _warn_if_child_is_bigger_than_padding_view(self):
        """
        print warning if child is bigger than padding.
        :return: nothing
        """
        p_height = self._padding_view_height
        p_width = self._padding_view_width

        c_height = self._child.get_height()
        c_width = self._child.get_width()

        if p_height < c_height or p_width < c_width:
            warnings.warn("Child's size is bigger than parent", Warning)

    def generate(self) -> Image:
        """
        generate image file based on attribute of this object
        :return: an Image.
        """
        parent = self._make_background()
        if self._child is not None:
            aligned_child = self._make_aligned_child()

            if aligned_child is None:
                pass
            child_padding = self._child.get_padding()
            parent.paste(
                aligned_child,
                box=(child_padding.left, child_padding.top),
                mask=aligned_child
            )

        return parent

    def _make_aligned_child(self) -> Image:
        if self._child is None:
            return None

        self._warn_if_child_is_bigger_than_padding_view()

        child_img = self._child.generate()
        child_padding = self._child.get_padding()
        virtual_view_for_child_alignment = Image.new(
            "RGBA",
            (self._padding_view_width, self._padding_view_height),
            color=(0, 0, 0, 0)
        )
        virtual_view_for_child_alignment.paste(child_img, self._get_alignment(), child_img)
        return virtual_view_for_child_alignment

    def _make_background(self) -> Image:
        return Image.new(mode="RGBA", size=(
            self._width, self._height), color=self._background.get_RGBA_by_tuple())
