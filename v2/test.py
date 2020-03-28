from fight import fight
from alice import alice
from elwing import elwing
from william import william
import cProfile
#william(6000,10000,400000)
def sort_by_range(champ):
    return champ.rang
l1 = [alice(244700,1,140000,1,2400000),elwing(244700,1,140000,1,2400000),william(140000,1,160000,1,2800000)]
l1.sort(key=sort_by_range)
l2 = [william(140000,1,160000,1,2800000),alice(244700,1,140000,1,2400000),elwing(244700,1,140000,1,2400000)]
l2.sort(key=sort_by_range)
a = fight(l1,l2)
#a.run()

'''
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
            champ = eval('a.t'+str(i//3+1)+'origin')[i%3]
            print(champ.name+'\t'+str(champ.hp)+'/'+str(champ.hp_limit))
            print(tmp)


'''
filename = input('输入保存战报的文件名，若已存在将覆盖写入(***.txt): ')
f1 = open(filename,'w') 
#f1 = open('战报.txt','w')
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
            champ = eval('a.t'+str(i//3+1)+'origin')[i%3]
            f1.write(champ.name+'\t'+str(champ.hp)+'/'+str(champ.hp_limit)+'\n')
            f1.write(tmp+'\n')
f1.close()
