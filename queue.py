"""queue module."""
from typing import List


class Queue:
    """Queue class"""
    def __init__(self, length: int = 0):
        """queue constructor."""
        self.queue: List = []
        self.length = length

    def push(self, data: int):
        """adds an element to the end of the queue."""
        if self.length and self.length <= len(self.queue):
            raise IndexError
        return self.queue.append(data)

    def pop(self) -> int:
        """removes the element at the beginning of the queue."""
        return self.queue.pop(0)
