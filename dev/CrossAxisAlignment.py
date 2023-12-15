from enum import Enum


class CrossAxisAlignmentFactory:
    @staticmethod
    def make(background_length: int, children_lengths: list[int]):
        raise NotImplementedError()


class Center(CrossAxisAlignmentFactory):
    @staticmethod
    def make(background_length: int, children_lengths: list[int]):
        return [(background_length - i) // 2 for i in children_lengths]


class Start(CrossAxisAlignmentFactory):
    @staticmethod
    def make(background_length: int, children_lengths: list[int]):
        return [0 for i in children_lengths]


class End(CrossAxisAlignmentFactory):
    @staticmethod
    def make(background_length: int, children_lengths: list[int]):
        return [background_length - i for i in children_lengths]


class CrossAxisAlignment(Enum):
    center = Center
    start = Start
    end = End
