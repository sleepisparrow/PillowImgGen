import unittest
from unittest import *

from dev.AxisAlignment import AxisAlignment
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

    def test_column_MainAxisAlignment_end(self):
        """
        MainAxisAlignment_end를 할 경우, 제일 밑에서 위로 올라가며 생성되는가?
        """
        column = Column(
            width=100,
            height=300,
            background=Colors.white,
            children=[
                View(
                    width=100,
                    height=100,
                    background=Colors.black,
                ),
                View(
                    width=100,
                    height=100,
                    background=Colors.blue,
                ),
            ],
            main_axis_alignment=AxisAlignment.end,
        )

        image = column.generate()
        # 위 100픽셀이 white?
        self.assertTrue(TestView.is_section_colored(0, 0, 100, 100, image, Colors.white))
        # 중간 픽셀이 black?
        self.assertTrue(TestView.is_section_colored(100, 0, 100, 200, image, Colors.black))
        # 마지막 100픽셀이 blue?
        self.assertTrue(TestView.is_section_colored(200, 0, 100, 300, image, Colors.blue))

    def test_column_MainAxisAlignment_space_around(self):
        """
        mainAxisAlignment을 space around로 하게 되면,
        객체간은 같은 거리, 객체와 벽 사이는 절반의 거리를 가지게 되는가?
        :return:
        """
        column = Column(
            width=100,
            height=600,
            background=Colors.white,
            children=[
                View(
                    width=100,
                    height=100,
                    background=Colors.red,
                ),
                View(
                    width=100,
                    height=100,
                    background=Colors.green,
                ),
                View(
                    width=100,
                    height=100,
                    background=Colors.blue,
                )
            ],
            main_axis_alignment=AxisAlignment.space_around
        )

        image = column.generate()
        target_color = [Colors.white, Colors.red, Colors.white, Colors.green, Colors.white, Colors.blue, Colors.white]
        target_y = [0, 50, 150, 250, 350, 450, 550, 600]
        for i in range(len(target_color)):
            self.assertTrue(TestView.is_section_colored(0, target_y[i], 100, target_y[i+1], image, target_color[i]))

    def test_column_MainAxisAlignment_space_evenly(self):
        column = Column(
            width=100,
            height=500,
            background=Colors.white,
            main_axis_alignment=AxisAlignment.space_evenly,
            children=[
                View(
                    width=100,
                    height=100,
                    background=Colors.red,
                ),
                View(
                    width=100,
                    height=100,
                    background=Colors.green,
                )
            ],
        )

        image = column.generate()
        target_color = [Colors.white, Colors.red, Colors.white, Colors.green, Colors.white]
        target_y = [0, 100, 200, 300, 400, 500]
        for i in range(len(target_color)):
            self.assertTrue(TestView.is_section_colored(0, target_y[i], 100, target_y[i + 1], image, target_color[i]))

    def test_column_MainAxisAlignment_space_between(self):
        column = Column(
            width=100,
            height=500,
            background=Colors.white,
            main_axis_alignment=AxisAlignment.space_between,
            children=[
                View(
                    width=100,
                    height=100,
                    background=Colors.red,
                ),
                View(
                    width=100,
                    height=100,
                    background=Colors.green,
                ),
                View(
                    width=100,
                    height=100,
                    background=Colors.blue,
                )
            ],
        )

        image = column.generate()
        target_color = [Colors.red, Colors.white, Colors.green, Colors.white, Colors.blue]
        target_y = [0, 100, 200, 300, 400, 500]
        for i in range(len(target_color)):
            self.assertTrue(TestView.is_section_colored(0, target_y[i], 100, target_y[i + 1], image, target_color[i]))
        pass


if __name__ == "main":
    unittest.main()
