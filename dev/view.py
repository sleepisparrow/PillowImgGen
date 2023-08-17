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
        if not isinstance(child, View):
            raise TypeError(f"child must be subclass of View but you give {type(child)}")

        self.__child = child
        self.__background = background
        self.width = width
        self.height = height

    def generate(self):
        # TODO: 여기에 자식이 잘 형성되도록 만들기
        return Image.new(mode="RGBA", size=(self.width, self.height), color=self.background.get_RGBA_by_tuple())
