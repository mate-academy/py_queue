"""
Implement FIFO
"""

class Queue:
    """Class FIFO"""
    def __init__(self, length=None):
        self.length = length
        self.queue = []

    def push(self, value: int):
        """Push values"""
        if self.length and len(self.queue) == self.length:
            raise IndexError
        self.queue.append(value)

    def pop(self) -> int:
        """Pop values"""
        return self.queue.pop(0)
