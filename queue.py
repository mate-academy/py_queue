"""FIFO Queue"""


class Queue:
    """Queue class"""
    def __init__(self, length=None):
        self.arr = []
        self.length = length

    def push(self, value: int):
        """Check length before add new item"""
        if len(self.arr) == self.length:
            raise IndexError
        self.arr.append(value)

    def pop(self) -> int:
        """Remove first item"""
        if not self.arr:
            raise IndexError
        return self.arr.pop(0)
