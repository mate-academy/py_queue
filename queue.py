class Queue:
    def __init__(self, length=0):
        self.queue = []
        self.length = length

    def push(self, value: int):
        if self.length and len(self.queue) >= self.length:
            raise IndexError
        print(self.queue)
        self.queue.append(value)

    def pop(self) -> int:
        print(self.queue)
        return self.queue.pop(0)
