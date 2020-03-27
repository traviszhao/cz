from fight import fight
from alice import alice
l1 = [alice(10000,5000,200000)]
l2 = [alice(8000,4000,100000)]
a = fight(l1,l2)
f1 = open('战报.txt','w')
try:
    a.run()

except Exception:
    f1.write(a.string+'\n')
    lst = ['蓝色方','紫色方']
    for i in range(0,6):
        if (i)%3 ==0:
            f1.write(lst[i//3]+'\n')
        tmp = eval('a.r'+str(i+1))
        if len(tmp)!=0:
            f1.write(eval('l'+str(i//3+1))[i%3].name+'\n')
            f1.write(tmp+'\n')
f1.close()
        