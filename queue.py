"""
queue
"""
from typing import List
from builtins import int


class Queue:
    """
    push
    pop
    """
    def __init__(self, length: int = 0):
        self.data: List[int] = []
        self.size = length

    def push(self, value: int):
        """

        :param value: int value to push
        :return: None
        """
        if self.size == len(self.data) and self.size:
            raise IndexError

        self.data.append(value)

    def pop(self) -> int:
        """
        :return: deleted element
        """
        return self.data.pop(0)
