'''
Module Queue
'''


class Queue:
    '''
    class  Queue
    '''
    def __init__(self, lngth=0):
        '''

        :param length:
        '''
        self.data = []
        self.lngth = lngth

    def push(self, value: int):
        '''

        :param value:
        :return:
        '''
        if self.lngth and len(self.data) >= self.lngth:
            raise IndexError
        self.data.append(value)

    def pop(self) -> int:
        '''

        :return:
        '''
        return self.data.pop(0)
