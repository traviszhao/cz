from fight import fight
from alice import alice
from elwing import elwing
from william import william
#william(6000,10000,400000)
l1 = [alice(10000,6000,300000),william(6000,10000,400000)]
l2 = [alice(10000,6000,300000),william(6000,10000,400000),elwing(10000,6000,300000)]
a = fight(l1,l2)
#a.run()

try:
    a.run()
except Exception:
    print(a.string)
    lst = ['蓝色方','紫色方']
    for i in range(0,6):
        if (i)%3 ==0:
            print(lst[i//3])
        tmp = eval('a.r'+str(i+1))
        if len(tmp)!=0:
            champ = eval('l'+str(i//3+1))[i%3]
            print(champ.name+'\t'+str(champ.hp)+'/'+str(champ.hp_limit))
            print(tmp)


'''
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
'''