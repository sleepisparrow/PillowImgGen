from unittest import TestCase

from PIL import Image

from dev.Color import Colors
from dev.imageView import ImageView
from test.test_view import TestView


class TestIamgeView(TestCase):
    def test_image_view_local_path(self):
        # 경로는 상대, 절대 모두 확인할 필요는 없다. (어차피 Image.open할 것이기에)
        path = "/home/tiredpiru/PycharmProjects/PillowImgGen/test/test_image/bottom_right.png"
        size = Image.open(path).size
        imageView = ImageView(image=path)
        self.assertEqual(size[0], imageView.get_width())
        self.assertEqual(size[1], imageView.get_height())

    def test_image_view_url(self):
        # 디스코드의 임의의 이미지를 이용해 테스트를 진행함
        path = "/home/tiredpiru/PycharmProjects/PillowImgGen/test/test_image/bottom_right.png"
        url = "https://cdn.discordapp.com/attachments/1014779651010334800/1151702833641554020/bottom_right.png"
        imageView = ImageView(image=url)
        size = Image.open(path).size
        self.assertEqual(size[0], imageView.get_width())
        self.assertEqual(size[1], imageView.get_height())
