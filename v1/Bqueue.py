class BoundedQueue:
    def __init__(self, capacity):
        assert isinstance(capacity, int), ('Error: Type error: %s' % (type(capacity)))
        assert capacity >= 0, ('Error: Illegal capacity: %d' % (capacity))         
        self.__items = []
        self.__capacity = capacity
    def enqueue(self, item):
        if len(self.__items) >= self.__capacity:
            raise Exception('Error: Queue is full')
        self.__items.append(item)
    def dequeue(self):
        if len(self.__items) <= 0:
            raise Exception('Error: Queue is empty')
        return self.__items.pop(0)
    def peek(self):
        if len(self.__items) <= 0:
            raise Exception('Error: Queue is empty')
        return self.__items[0]
    def isEmpty(self):
        return len(self.__items) == 0
    '''
    def isFull(self):
        return len(self.__items) == self.__capacity
    def size(self):
        return len(self.__items)
    def capacity(self):
        return self.__capacity
    '''
    def clear(self):
        self.__items = []
    def reduce(self):
        self.__items[0][0]-=1
        if self.__items[0][0] == 0:
            return self.dequeue()
    def __str__(self):
        str_exp = ""
        for item in self.__items:
            str_exp += (str(item) + " ,")
        return str_exp    