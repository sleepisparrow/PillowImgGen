from typing import List
from enum import Enum, auto
from PIL import Image
from dev.view import View


class AxisAlignmentFactory:
    # 배치할 좌표값들을 반환해야 하지, 이미지 그 자체를 반환하는 식으로 짜면, 코드가 굉장히 복잡해진다.
    # 배경의 길이랑, 자식의 길이들을 받아서, 각 child의 좌표 리스트를 반환하도록 짜자.
    @staticmethod
    def make(background_length: int, children_lengths: list[int]) -> list[int]:
        raise NotImplementedError("package error occured. please report")


class Start(AxisAlignmentFactory):
    @staticmethod
    def make(background_length: int, children_lengths: list[int]) -> list[int]:
        ret = []
        curr = 0
        for i in children_lengths:
            ret.append(curr)
            curr += i
        return ret


class End(AxisAlignmentFactory):
    @staticmethod
    def make(background_length: int, children_lengths: list[int]) -> list[int]:
        # 뒤에서부터 올려가면서 계산하고, 마지막에 reverse
        value = background_length
        ret = []
        
        l = len(children_lengths)
        for i in range(l):
            value -= children_lengths[l-i-1]
            ret.append(value)
        ret.reverse()
        return ret

class AxisAlignment(Enum):
    start = Start
    end = End
    space_around = auto()
    space_between = auto()
    space_evenly = auto()

# TODO: 저거 그냥 auto 대신에 팩토리 메서드 패턴을 응용해서 만들어서 코드짜기
