from unittest import *

from dev.Color import Colors
from dev.Column import Column
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

    def test_column_children_padding(self):
        """
        column 안의 자식들의 padding이 잘 적용되어 나타나는가?
        --------------------------------
        1. red 사각형 (80*80, padding: 모든 방향으로 10씩)
        2. green 사각형(80*100, padding: vertical 방향으로 10씩)
        :return:
        """
        column = Column(
            width=200,
            height=200,

        )

