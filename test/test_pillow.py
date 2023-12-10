from io import BytesIO
from unittest import TestCase
from PIL import Image
import requests

from dev.Color import Colors


class TestPillow(TestCase):
    def test_resize(self):
        original = Image.open('/home/tiredpiru/PycharmProjects/PillowImgGen/test/test_image/center.png')
        sample = original.resize((200, 200))
        sample2 = original.resize((50, 100))

    def test_crop(self):
        original = Image.open('/home/tiredpiru/PycharmProjects/PillowImgGen/test/test_image/center.png')
        sample = original.crop((0, 0, 200, 200))
        # 크롭을 원본보다 크게 하면 이미지가 비어버리게 된다.

    def test_url(self):
        response = requests.get('https://cdn.discordapp.com/attachments/1014779651010334800/1125051387638722610/img.png')
        img = Image.open(BytesIO(response.content))