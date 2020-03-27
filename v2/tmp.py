class fight():
    def __init__(self):        #蓝色方队伍 紫色方队伍
        self.data = ''
        self.string = ''
        self.r1 = '1'
        self.r2 = '2'
        self.r3 = '3'
        self.r4 = '4'
        self.r5 = '5'
        self.r6 = '6'
    def __str__(self):
        tmp = ''
        for i in range(1,7):
            tmp += eval('self.r'+str(i))+'\n'
        return tmp
a = fight()
print(a)