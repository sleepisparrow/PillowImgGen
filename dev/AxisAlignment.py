from enum import Enum


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
            value -= children_lengths[l - i - 1]
            ret.append(value)
        ret.reverse()
        return ret


def _make_space_array(start: int, margin: int, children_lengths: list[int]) -> list[int]:
    """
    space어쩌고 만들때 쓰는 메서드
    :param start:
    :param margin:
    :param children_lengths:
    :return:
    """
    ret = []
    for i in children_lengths:
        ret.append(start)
        start += i + margin
    return ret


class SpaceAround(AxisAlignmentFactory):
    @staticmethod
    def make(background_length: int, children_lengths: list[int]) -> list[int]:
        empty_length = background_length  # empty_length = 여유가 되는 거리
        for i in children_lengths:
            empty_length -= i
        margin = empty_length // len(children_lengths)  # margin = 객체 간 거리

        return _make_space_array(margin//2, margin, children_lengths)


class SpaceEvenly(AxisAlignmentFactory):
    @staticmethod
    def make(background_length: int, children_lengths: list[int]) -> list[int]:
        empty_length = background_length  # empty_length = 여유가 되는 거리
        for i in children_lengths:
            empty_length -= i
        margin = empty_length // (len(children_lengths) + 1)  # margin = 객체 간 거리

        return _make_space_array(margin, margin, children_lengths)


class SpaceBetween(AxisAlignmentFactory):
    @staticmethod
    def make(background_length: int, children_lengths: list[int]) -> list[int]:
        empty_length = background_length  # empty_length = 여유가 되는 거리
        for i in children_lengths:
            empty_length -= i
        margin = empty_length // (len(children_lengths) - 1)  # margin = 객체 간 거리

        return _make_space_array(0, margin, children_lengths)


class AxisAlignment(Enum):
    start = Start
    end = End
    space_around = SpaceAround
    space_between = SpaceBetween
    space_evenly = SpaceEvenly
