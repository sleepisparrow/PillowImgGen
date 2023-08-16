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

    def test_is_section_colored(self):
        """
        is_section_colored를 테스트. fx, fy 부터 tx, ty 전까지가 모두 color의 색깔을 가지고 있는지에 대해서 알아본다.
        :return:
        """
        right_image = Image.open("./only_white.png")
        wrong_image = Image.open("./has_blue.png")

        self.assertFalse(self.is_section_colored(0, 0, 400, 300, wrong_image, Color(0xff, 0xff, 0xff)))
        self.assertTrue(self.is_section_colored(0, 0, 400, 300, right_image, Color(0xff, 0xff, 0xff)))

    @staticmethod
    def is_section_colored(fx: int, fy: int, tx: int, ty: int, img: Image, color: Color):
        """
        완전 탐색으로, (fx, fy)부터 (tx, ty)까지의 영역이 모두 color 색인지 조사한다.
        :param fx: 시작 x좌표
        :param fy: 시작 y좌표
        :param tx: 끝 x좌표
        :param ty: 끝 y좌표
        :param img: 조사할 사진
        :param color: 타겟으로 하는 색
        :return: 모두 같은 색인지에 대한 여부
        """
        px = img.load()
        target_color = color.get_RGB_by_tuple()
        for i in range(fx, tx):
            for j in range(fy, ty):
                if px[i, j] != target_color:
                    return False

        return True
