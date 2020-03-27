class BoundedQueue:
    def __init__(self):  
        self.__items = []
    def enqueue(self, item):
        self.__items.append(item)
    def dequeue(self):
        if len(self.__items) <= 0:
            raise Exception('Error: Queue is empty')
        return self.__items.pop(0)
    def isEmpty(self):
        return len(self.__items) == 0
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