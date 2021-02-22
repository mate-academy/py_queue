"""class FIFO module"""


class Queue:
    """class FIFO"""
    def __init__(self, length=0):
        self.array = []
        self.maxlength = length

    def push(self, value: int):
        """
        Function for check array length and push new element.
        :param value: new element
        :return: None
        """
        if self.maxlength and len(self.array) >= self.maxlength:
            raise IndexError
        self.array.append(value)

    def pop(self) -> int:
        """
        function for remove first element from array
        :return: removed element
        """
        return self.array.pop(0)
