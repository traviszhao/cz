from fight import fight
from alice import alice
from elwing import elwing
from william import william
import cProfile


def sort_by_range(champ):
    return champ.rang
strd = {1:'爱丽丝',2:'威廉丶姆斯兰',3:'艾尔薇'}
str_dct = [(k,strd[k]) for k in sorted(strd.keys())] 
champ_dct = {1:'alice',2:'william',3:'elwing'}
def get_champ():
    print(str(str_dct))
    while True:
        try:
            ind = int(input('输入英雄序号(数字): ').strip())
            champ_name = champ_dct[ind]
            break
        except:
            print('Invalid input, please try again. ')
    while True:
        try:
            a = input('面板攻击(整数,1-40w): ')
            a = int(a)
            if a not in range(1,400001):
                raise
            break
        except:
            print('Invalid input, please trhy again. ')
    while True:
        try:
            ar = input('进场攻buff(小数,0.3-2.0): ')
            ar = float(ar)
            if ar <0.3 or ar>2.0:
                raise
            break
        except:
            print('Invalid input, please try again. ')
    while True:
        try:
            d = input('面板防御(整数,0-30w): ')
            d = int(d)
            if d <0 or d>300000:
                raise
            break
        except:
            print('Invalid input, please try again. ')
    while True:
        try:
            dr = input('进场防御buff(小数,1.0-1.8): ')
            dr = float(dr)
            if dr <1.0 or dr>1.8:
                raise
            break
        except:
            print('Invalid input, please try again. ')
    while True:
        try:
            hp = input('血量(整数,100w-400w): ')
            hp = int(hp)
            if hp<1000000 or hp>4000000:
                raise
            break
        except:
            print('Invalid input, please try again. ')
     
    champ = eval(champ_name+'('+str(a)+','+str(ar)+','+str(d)+','+str(dr)+','+str(hp)+')')
    print(champ_name+'('+str(a)+','+str(ar)+','+str(d)+','+str(dr)+','+str(hp)+') has been created')
    return champ
'''
l1 = []
print('现在为蓝色方（左手）选择英雄')
for i in range(3):
    l1.append(get_champ())
    for champ in l1:
        print(champ)

l2 = []
print('现在为紫色方（右手）选择英雄')
for i in range(3):
    l2.append(get_champ())


'''
l1 = [alice(244700,1,140000,1,2400000),elwing(244700,1,140000,1,2400000),william(140000,1,160000,1,2800000)]

l2 = [william(140000,1,160000,1,2800000),alice(244700,1,140000,1,2400000),elwing(244700,1,140000,1,2400000)]

l1.sort(key=sort_by_range)
l2.sort(key=sort_by_range)

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
'''