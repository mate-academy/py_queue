"""module docstring"""
class Queue:
    """class docstring"""

    def __init__(self, length=None):
        """def docstring"""
        self.array = []
        self.length = length

    def push(self, value):
        """def docstring"""
        if len(self.array) == self.length and self.length is not None:
            raise IndexError
        self.array.append(value)

    def pop(self):
        """def docstring"""
        if not self.array:
            raise IndexError
        return self.array.pop(0)
