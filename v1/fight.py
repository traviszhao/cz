import random
from Bqueue import BoundedQueue as queue
def dmg(a,d,e):
    ran = random.randint(-3,3)
    ratio = (100+ran)/100
    return a**2/(a+d)*e*ratio
def get_random_time():
    return random.randint(0,4)
def change_state(champ,index,amount):
    if index == 1:
        champ.a += amount
    if index == 2:
        champ.d *= (1+amount)
    if index == 3:
        champ.hp += amount
    if index == 4:
        champ.dodge *= amount
class fight():
    def __init__(self,blue,red):        #蓝色方队伍 紫色方队伍
        self.t1 = blue
        self.t2 = red
        self.data = ''
        self.string = ''
        self.r1 = ''
        self.r2 = ''
        self.r3 = ''
        self.r4 = ''
        self.r5 = ''
        self.r6 = ''
        #每个角色单独的战报记录 记录所有事件(动作，造成伤害，承受伤害) {时间:事件}
        #6人 暂不支持召唤物
    def __str__(self):
        return self.string
    def __repr__(self):
        return self.data
    
    def get_spell(self,champ,ls):
        ls.clear()
        spell = champ.genspell()
        self.string+='蓝色方'+ champ.name+': '+spell[0]+'\n'
        time1, time2 = spell[1],spell[2]
        time1+= get_random_time()
        ls.enqueue([time1,spell])
        ls.enqueue([time2,None])    
        
    def cast_spell(self,champ,spell,team): #['甜蜜梦境',5,0,[1,300,5,(4,0.7)]]
        data = spell[-1]
        a = champ.a
        enemyteam = []
        teams = ['蓝色方的','紫色方的']
        current,oppo = teams[team],teams[1-team]
        for enemy in eval('self.t'+str(2-team)):
            enemyteam.append(enemy)
        for i in range(len(data)):
            defender = []
            if i%2 == 0:
                if data[i] == 1:
                    defender.append(enemyteam[0])
                if data[i] == 2:
                    defender = enemyteam    
            for enemy in defender:
                damage = min(round(dmg(a,enemy.d,data[i+1]/100)),enemy.hp)
                self.string+= current+ champ.name+' 使用的 ' +spell[0] +' 对 '+ oppo +enemy.name+ ' 造成了 ' + str(damage)+ '的伤害\n'
                change_state(enemy,3,-1*damage)
                self.string += oppo+ enemy.name + '剩余' +str(enemy.hp) +'/'+str(enemy.hp_limit) + 'hp\n'
                if enemy.hp == 0:
                    self.string += current +champ.name +'击杀了' +oppo +enemy.name
                    enemyteam.remove(enemy)
                    if len(enemyteam) == 0:
                        raise 
        
    def get_attack(self,champ,ls):
        attack = champ.basic_attack
        time1, time2 = attack[1],attack[2]
        time1+= get_random_time()
        ls.enqueue([time1,attack])
        ls.enqueue([time2,None])                    
                        
    def run(self):
        #temp queue 记录每个角色即将发生的事件 [剩余时间,事件] 剩余时间循环 -1
        l1 = queue(60)
        l2 = queue(60)
        l3 = queue(60)
        l4 = queue(60)
        l5 = queue(60)
        l6 = queue(60)
        for i in range(0,1800):         #时间上限150秒，即25回合
            if i != 0 and i%60==0:      #能量条清空
                self.string+='\n'
                for champ in self.t1:
                    tmp = eval('l'+str(self.t1.index(champ)+1))
                    self.get_spell(champ,tmp)
                for champ in self.t2:
                    tmp = eval('l'+str(self.t2.index(champ)+4))
                    self.get_spell(champ,tmp)
            else:
                for champ in self.t1:
                    count = str(self.t1.index(champ)+1)
                    tmp = eval('l'+count)
                    if tmp.isEmpty():
                        self.get_attack(champ,tmp)                
                    else:
                        a = tmp.reduce()
                        if a :
                            spell = a[1]
                            if spell:
                                self.cast_spell(champ,spell,0)
                                self.record(count,i/10,spell)
                for champ in self.t2:
                    count = str(self.t2.index(champ)+4)
                    tmp = eval('l'+count)
                    if tmp.isEmpty():
                        self.get_attack(champ,tmp)
                    else:
                        a = tmp.reduce()
                        if a:
                            spell = a[1]
                            if spell:
                                self.cast_spell(champ,spell,1)
                                self.record(count,i/10,spell)
    def record(self,count,t,info):
        tmp = str(t)+'\t'
        for element in info:
            tmp += str(element)+' '
        tmp += '\n'
        if count =='1':
            self.r1+=tmp
        if count =='2':
            self.r2+=tmp
        if count =='3':
            self.r3+=tmp
        if count =='4':
            self.r4+=tmp
        if count =='5':
            self.r5+=tmp
        if count =='6':
            self.r6+=tmp

                    