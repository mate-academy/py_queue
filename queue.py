"""docstring"""
class Queue:
    """
    Defines the "Queue" data structure,
    based on list type object.
    """
    def __init__(self, length=0):
        self.queue = []
        self.length = length

    def push(self, value: int):
        """
        Adds new element in the end af the Queue
        :param value: int
        """
        if self.length:
            if len(self.queue) == self.length:
                raise IndexError
        self.queue.append(value)

    def pop(self) -> int:
        """
        Returns first element from the Queue
        :return: int
        """
        return self.queue.pop(0)
