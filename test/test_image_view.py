from unittest import TestCase

from PIL import Image

from dev.Color import Colors
from dev.alignment import Alignment
from dev.imageOption import ImageOption
from dev.imageView import ImageView
from dev.view import View
from test_view import TestView


class TestIamgeView(TestCase):
    path = "/home/tiredpiru/PycharmProjects/PillowImgGen/test/test_image/bottom_right.png"

    def test_image_view_local_path(self):
        # 경로는 상대, 절대 모두 확인할 필요는 없다. (어차피 Image.open할 것이기에)
        path = "/home/tiredpiru/PycharmProjects/PillowImgGen/test/test_image/bottom_right.png"
        size = Image.open(path).size
        image_view = ImageView(path=path)
        self.assertEqual(size[0], image_view.get_width())
        self.assertEqual(size[1], image_view.get_height())

    def test_image_view_url(self):
        # 디스코드의 임의의 이미지를 이용해 테스트를 진행함
        url = "https://cdn.discordapp.com/attachments/1014779651010334800/1151702833641554020/bottom_right.png"
        image_view = ImageView(path=url)
        size = Image.open(self.path).size
        self.assertEqual(size[0], image_view.get_width())
        self.assertEqual(size[1], image_view.get_height())

    def test_image_view_fill(self):
        """
        fill 옵션을 사용하는 경우, 이미지가 적절히 확대되어 나타나지는가?
        :return:
        """
        # fill 옵션을 사용한 경우, 자기가 가지고 있는 이미지가  채워지도록 해라 였나?
        image_view = ImageView(
            width=400,
            height=400,
            path="/home/tiredpiru/PycharmProjects/PillowImgGen/test/test_image/center.png",
            image_option=ImageOption.fill,
        )
        image = image_view.generate()
        size = image.size
        self.assertEqual(size[0], 400)
        self.assertEqual(size[1], 400)

        image.show()
        # 이미지를 확장하게 되면, 단순히 커지는게 아닌 blur 처리가 되기 때문에 테스트할 수 없음.

        # width, height가 path보다 작으면, 그냥 알아서 crop되는게 아닐까?
    def test_image_view_crop_left_top(self):
        """
        crop 을 진행한 경우, left_top을 기준으로 잘 crop되는가?
        :return:
        """
        path = "./test_image/center.png"
        image = ImageView(
            width=50,
            height=50,
            path=path,
            image_option=ImageOption.crop
        )

        image = image.generate()
        size = image.size
        self.assertEqual(size[0], 50)
        self.assertEqual(size[1], 50)

        TestView.is_only_box_colored(25, 25, 50, 50, image, Colors.white, Colors.red)

    def test_child_showed_normally(self):
        """
        자식이 있는 경우, 자식이 제대로 보여지는가?
        :return:
        """
        image_view = ImageView(
            width=200,
            height=200,
            path="test_image/center.png",
            image_option=ImageOption.fill,
            child=View(
                width=100,
                height=100,
                background=Colors.blue,
            ),
            alignment=Alignment.center,
        )
        image = image_view.generate()

        rst = TestView.is_section_colored(
            fx=50,
            fy=50,
            tx=150,
            ty=150,
            img=image,
            color=Colors.blue
        )
        self.assertTrue(rst)

        # TODO: test image view
        # 이미지 뷰 crop옵션 9개는 어떻게 해야 하는가?
