"""Implement FIFO queue according to the given interface. Queue must have a limited length."""
from typing import List

class Queue:
    """FIFO queue implementation"""
    def __init__(self, length: int = 0):
        """Docstring init"""
        self.array: List[int] = []
        self.length = length

    def push(self, value: int):
        """Pushing value to the end of array"""
        if self.length and self.length <= len(self.array):
            raise IndexError
        self.array.append(value)

    def pop(self) -> int:
        """Method removes the last element from an array"""
        return self.array.pop(0)
