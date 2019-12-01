"""docstring"""

class Queue:
    """init queue structure"""
    def __init__(self, length=None):
        """init"""
        self.items = []
        self.length = length

    def push(self, value: int):
        """add new element"""
        if self.length and len(self.items) == self.length:
            raise IndexError
        self.items.append(value)

    def pop(self) -> int:
        """return first element"""
        return self.items.pop(0)
