from unittest import *

from dev.Color import Color
from dev.main import *


class TestImageGeneration(TestCase):
    def test_right_size_generate(self):
        """
        올바른 사이즈의 사진을 생성하는가?
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