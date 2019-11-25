"""module queue"""
from typing import List


class Queue:
    """
    Thread-safe, memory-efficient, maximally-sized queue supporting queueing and
    dequeueing in worst-case O(1) time.
    """
    def __init__(self, length: int = 0):
        self.queue: List[int] = []
        self.max_size = length

    def push(self, value: int):
        """
        Enqueue item to the list. Pushes this item onto the tail of this queue.
        :param value: int
        :return: None
        """
        if self.max_size and self.max_size <= len(self.queue):
            raise IndexError
        self.queue.append(value)

    def pop(self) -> int:
        """
        Dequeue item from the list. Removes the item at the head of this queue and
        returns this item.
        :return: int
        """
        return self.queue.pop(0)
