from unittest import *
import unittest

from dev.Color import Colors
from dev.Column import Column
from dev.padding import Padding
from dev.view import View
from test_view import TestView


class TestColumn(TestCase):
    def test_column(self):
        """
        Column을 생성하고, 여러개의 객체를 넣을 경우, 위부터 차례로 정렬되는가?
        :return:
        """
        column = Column(
            width=100,
            height=300,
            background=Colors.white,
            children=[
                View(
                    width=100,
                    height=100,
                    background=Colors.red,
                ),
                View(
                    width=100,
                    height=50,
                    background=Colors.green,
                ),
                View(
                    width=100,
                    height=100,
                    background=Colors.blue
                )
            ],
        )

        image = column.generate()
        self.assertTrue(TestView.is_section_colored(0, 0, 100, 100, image, Colors.red))
        self.assertTrue(TestView.is_section_colored(0, 100, 100, 150, image, Colors.green))
        self.assertTrue(TestView.is_section_colored(0, 150, 100, 250, image, Colors.blue))
        self.assertTrue(TestView.is_section_colored(0, 250, 100, 300, image, Colors.white))

if __name__ == "main":
    unittest.main()