from unittest import *

from PIL import Image

from dev.Color import Color
from dev.view import View


class TestView(TestCase):
    def test_view_generate_right_image_size(self):
        """
        뷰를 생성하였을 때, 그 크기에 맞는 이미지가 나오는가?
        :return:
        """
        width = 400
        height = 300
        view = View(width=width, height=height)
        img = view.generate()
        x, y = img.size
        self.assertEquals(width, x)
        self.assertEquals(height, y)

    def test_empty_view_generate_empty_image(self):
        """
        뷰에 배경색을 부여하지 않았을 때, 투명한 이미지가 나오는가?
        :return:
        """
        width = 400
        height = 300
        # setting
        view = View(width=width, height=height)
        img = view.generate()
        px = img.load()  # for check each pixels
        for i in range(width):
            for j in range(height):
                self.assertEqual(px[i, j][3], 0)  # foruth one is transparency

    def test_generate_colored_image_when_view_has_color(self):
        """
        뷰에 배경색을 부여하였을 경우, 그 색에 맞는 이미지가 나오는가?
        :return:
        """
        view = View(width=400, height=300)
        img = view.generate()

    def is_section_colored(self, fx: int, fy: int, tx: int, ty: int, img: Image, color: Color):
        pass
