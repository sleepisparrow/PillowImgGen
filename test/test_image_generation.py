from unittest import *
from PIL import *

from dev.main import *


class TestImageGeneration(TestCase):
    def test_right_size_generate(self):
        """
        올바른 사이즈의 사진을 생성하는가?
        :return:
        """
        width = 400
        height = 300
        img = generate_image(400, 300)
        self.assertEquals(width, img.size[0])
        self.assertEquals(height, img.size[1])

    def test_exception_wrong_input(self):
        """
        잘못된 가로, 세로가 주어졌을 때, 잘 대처하는가?
        :return:
        """
        with self.assertRaises(ValueError):
            img = generate_image(-100, 200)
        with self.assertRaises(ValueError):
            img = generate_image(100, 0)

    def test_exception_wrong_type(self):
        """
        잘못된 타입이 들어온 경우, 잘 대처하는가?
        :return:
        """
        with self.assertRaises(TypeError) as context:
            img = generate_image(10.4, 10)
        print(context.exception)

    def test_after_image_is_empty(self):
        """
        이미지 생성 후 바로 나오게 된다면, 모두 비어 있는 상태인건가?
        :return:
        """
        width = 100
        height = 100
        img = generate_image(width, height)
        px = img.load()  # 픽셀 배열로 만드는 함수
        for i in range(width):
            for j in range(height):
                value = px[i, j][3]  # 4번째 값이 투명도이기 때문
                self.assertEquals(0, value)

    def test_empty_view_generate_image(self):
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

    # TODO: 컬러가 있는 경우, 모든 픽셀이 그 컬러로 색칠되어 나옴?
    # TODO: 자식이 있는 경우, 자식 역시 왼쪽 위 가장자리를 기준으로, witdth, height만큼 잘 구현됨?
    # TODO: 부모 view를 자식 view가 넘어서지 않음?