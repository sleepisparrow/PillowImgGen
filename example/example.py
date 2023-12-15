from dev.MainAxisAlignment import AxisAlignment
from dev.Color import Colors
from dev.Column import Column
from dev.imageView import ImageView
from dev.view import *

view = Column(
    width=100,
    height=300,
    background=Colors.white,
    main_axis_alignment=AxisAlignment.space_between,
    children=[
        View(
            width=100,
            height=100,
            background=Colors.green,
            child=ImageView(
                width=98,
                height=98,
                path="https://cdn.discordapp.com/attachments/1014779651010334800/1151702833641554020/bottom_right.png",
            ),
        ),
        View(
            width=100,
            height=100,
            background=Colors.blue,
        ),
    ]
)
img = view.generate()
img.show()
