from unittest import TestCase

import requests
from PIL import Image


class TestMethod(TestCase):
    def test_is_url_image(self):
        url = "https://cdn.discordapp.com/attachments/1091745240349671465/1152935309810610247/1694948160891.jpg"
        absolute_path = "/home/tiredpiru/PycharmProjects/PillowImgGen/test/test_image/only_white.png"
        image: Image = self.get_image(url)
        iamge2: Image = self.get_image(absolute_path)

    @staticmethod
    def get_image(path) -> Image:
        try:
            return Image.open(requests.get(path, stream=True).raw)
        except requests.exceptions.MissingSchema:
            return Image.open(path)
