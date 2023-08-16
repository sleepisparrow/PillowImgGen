class Color:
    def __init__(self, R: int, G: int, B: int, A: int = 255):
        if type(R) != int or type(G) != int or type(B) != int or type(A) != int:
            raise TypeError("R, G, B, A must be int value")
        if not 0 <= R <= 255:
            raise ValueError(f"R value must be between 0 to 255 but you give {R}")
        if not 0 <= G <= 255:
            raise ValueError(f"G value must be between 0 to 255 but you give {G}")
        if not 0 <= B <= 255:
            raise ValueError(f"B value must be between 0 to 255 but you give {B}")
        if not 0 <= A <= 255:
            raise ValueError(f"A value must be between 0 to 255 but you give {A}")

        self.__R = R
        self.__G = G
        self.__B = B
        self.__A = A

    def get_RGBA_by_tuple(self) -> tuple[int, int, int, int]:
        return self.__R, self.__G, self.__B, self.__A

    def get_RGB_by_tuple(self) -> tuple[int, int, int]:
        return self.__R, self.__G, self.__B


class Colors:
    white = Color(0xff, 0xff, 0xff)
    red = Color(0xff, 0, 0)
    green = Color(0, 0xff, 0)
    blue = Color(0, 0, 0xff)
    black = Color(0, 0,0)