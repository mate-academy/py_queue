"""
docstring
"""


class Queue:
    """
    class doc
    """
    def __init__(self, length=None):
        """

        :param length:
        """
        self.queue = []
        self.length = length

    def push(self, value: int):
        """

        :param value:
        :return:
        """
        if self.length and len(self.queue) == self.length:
            raise IndexError
        self.queue.append(value)

    def pop(self) -> int:
        """

        :return:
        """
        return self.queue.pop(0)
