class Padding:
    def __init__(self, left: int, top: int, right: int, bottom: int):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

    @staticmethod
    def fromLTRB(left: int, top: int, right: int, bottom: int):
        """
        make padding by left, top, right bottom and returns new padding
        :param left: padding to left side
        :param top: padding to top side
        :param right: padding to right side
        :param bottom: padding to bottom side
        :return:Padding
        """
        return Padding(left, top, right, bottom)

    @staticmethod
    def symmetric(horizontal: int, vertical: int):
        """
        makes padding. horizontal will be left and right, vertical will be top or bottom
        :param horizontal:
        :param vertical:
        :return:
        """
        return Padding(horizontal, vertical, horizontal, vertical)

    @staticmethod
    def all(value: int):
        """
        makes padding. value will be all side of padding
        :param value:
        :return:
        """
        return Padding(value, value, value, value)

