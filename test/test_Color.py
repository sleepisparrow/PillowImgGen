from dev.Color import Color
from unittest import *


class TestColor(TestCase):
    def test_Color_class_always_has_right_value(self):
        """
        Color 클래스에 이상한 값을 넣어도 에러가 발생하지 않는가?
        :return:
        """
        with self.assertRaises(TypeError):
            Color(0xff, 0xff, 1.11)

        with self.assertRaises(ValueError):
            Color(256, 1, 1)

        with self.assertRaises(ValueError):
            Color(-1, 1, 1)
