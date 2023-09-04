from dev.Color import Colors
from dev.view import *

view = View(
    width=100,
    height=100,
    background=Colors.white,
    alignment=Alignment.bottom_right,
    child=View(
        width=50,
        height=50,
        background=Colors.red
    )
)
img = view.generate()
img.save('bottom_right.png')
