import warnings
from unittest import *

from PIL import Image

from dev.Color import Color, Colors
from dev.view import View, Alignment


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
        view = View(width=400, height=300, background=Color(0xff, 0, 0))
        img = view.generate()
        self.assertTrue(self.is_section_colored(0, 0, 400, 300, img, Color(0xff, 0, 0)))

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
        if len(px[0, 0]) == 4:
            target_color = color.get_RGBA_by_tuple()
        else:
            target_color = color.get_RGB_by_tuple()
        for i in range(fx, tx):
            for j in range(fy, ty):
                if px[i, j] != target_color:
                    return False

        return True

    def test_if_child_exists_then_generate_make_child_in_left_top(self):
        """
        자식이 있고, 위치에 대한 내용이 없는 경우, 왼쪽 위에 생성이 되는가?
        :return:
        """
        parent_color = Colors.white
        child_color = Colors.red
        view = View(width=400,
                    height=300,
                    background=parent_color,
                    child=View(
                        width=100,
                        height=50,
                        background=child_color,
                    ),
                    )

        img = view.generate()
        is_child_colored = self.is_section_colored(0, 0, 100, 50, img, child_color)
        is_parent_colored_A = self.is_section_colored(100, 0, 400, 300, img, parent_color)
        is_parent_colored_B = self.is_section_colored(0, 50, 400, 300, img, parent_color)

        self.assertTrue(is_child_colored)
        self.assertTrue(is_parent_colored_A)
        self.assertTrue(is_parent_colored_B)

    def test_child_view_must_not_overflow_parent_view(self):
        """
        자식이 부모를 넘어서지 않는지 검사하기 + 부모보다 큰 자식이 있는 경우, 경고를 출력하는지를 조사하기
        :return:
        """
        biggest_color = Colors.white
        bigger_color = Colors.red
        smallest_color = Colors.blue
        with warnings.catch_warnings(record=True):
            view = View(width=400,
                        height=300,
                        background=biggest_color,
                        child=View(
                            width=200,
                            height=100,
                            background=bigger_color,
                            child=View(
                                width=300,
                                height=200,
                                background=smallest_color
                            ),
                        ),
                        )

        # 넘어서지 않는지 검증하는 부분
        img = view.generate()
        is_parent_filled = self.is_section_colored(0, 0, 200, 100, img, smallest_color)  # 부모를 다 채우긴 함?
        # 자식이 부모를 넘어서지 않음?
        is_child_doesnt_overflowed_1 = self.is_section_colored(200, 0, 400, 300, img, biggest_color)
        is_child_doesnt_overflowed_2 = self.is_section_colored(0, 100, 400, 300, img, biggest_color)

        self.assertTrue(is_parent_filled)
        self.assertTrue(is_child_doesnt_overflowed_1)
        self.assertTrue(is_child_doesnt_overflowed_2)

    def test_child_aligned_horizontal_center(self):
        """
        뷰에 정렬(alignment=Alignment.top_center)을 넣어줄 경우, 제일 위쪽 센터에 잘 정렬되는가?
        :return:
        """
        view = View(
            width=300,
            height=300,
            background=Colors.white,
            child=View(
                width=100,
                height=100,
                background=Colors.red,
            ),
            alignment=Alignment.top_center
        )
        img = view.generate()

        top_side = self.is_section_colored(100, 0, 200, 100, img, Colors.red)
        left_side = self.is_section_colored(0, 0, 100, 300, img, Colors.white)
        right_side = self.is_section_colored(200, 0, 300, 300, img, Colors.white)
        mid_side = self.is_section_colored(100, 100, 200, 300, img, Colors.white)

        self.assertTrue(top_side)
        self.assertTrue(left_side)
        self.assertTrue(right_side)
        self.assertTrue(mid_side)

    def test_top_right_alignment(self):
        """
        오른쪽 위 정렬이 잘 되는지 확인하는 테스트
        :return:
        """
        view = View(
            width=300,
            height=300,
            background=Colors.white,
            child=View(
                width=100,
                height=100,
                background=Colors.red,
            ),
            alignment=Alignment.top_right
        )
        img = view.generate()
        right_center = self.is_section_colored(0, 0, 200, 300, img, Colors.white)
        left_bottom = self.is_section_colored(200, 100, 300, 300, img, Colors.white)
        target = self.is_section_colored(200, 0, 300, 100, img, Colors.red)

        self.assertTrue(right_center)
        self.assertTrue(left_bottom)
        self.assertTrue(target)

    def test_align_center_left(self):
        """
        왼쪽 중앙에 배치가 잘 되었는지 확인하는 테스트
        :return:
        """
        view = View(
            width=300,
            height=300,
            background=Colors.white,
            child=View(
                width=100,
                height=100,
                background=Colors.red,
            ),
            alignment=Alignment.center_left
        )
        img = view.generate()
        top = self.is_section_colored(0, 0, 300, 100, img, Colors.white)
        target = self.is_section_colored(0, 100, 100, 200, img, Colors.red)
        middle = self.is_section_colored(100, 100, 300, 200, img, Colors.white)
        bottom = self.is_section_colored(0,200, 300, 300, img, Colors.white)

        self.assertTrue(top)
        self.assertTrue(target)
        self.assertTrue(middle)
        self.assertTrue(bottom)

    def test_align_bottom_left(self):
        """
            왼쪽 중앙에 배치가 잘 되었는지 확인하는 테스트
            :return:
        """
        view = View(
            width=300,
            height=300,
            background=Colors.white,
            child=View(
                width=100,
                height=100,
                background=Colors.red,
            ),
            alignment=Alignment.bottom_left
        )

        img = view.generate()

        top = self.is_section_colored(0,0,300,200,img,Colors.white)
        target = self.is_section_colored(0, 200, 100, 300, img, Colors.red)
        bottom = self.is_section_colored(100, 200, 300, 300, img, Colors.white)

        self.assertTrue(top)
        self.assertTrue(target)
        self.assertTrue(bottom)