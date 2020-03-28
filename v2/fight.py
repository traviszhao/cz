#击杀时count重新算

import random
from Bqueue import BoundedQueue as queue
teams = ['蓝色方的','紫色方的']
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
        self.t1origin = []
        self.t2origin = []
        for i in range(len(blue)):
            self.t1origin.append(blue[i])
        for i in range(len(red)):
            self.t2origin.append(red[i])        
        self.data = ''
        self.string = ''
        self.r1 = ''
        self.r2 = ''
        self.r3 = ''
        self.r4 = ''
        self.r5 = ''
        self.r6 = ''
        self.events = queue()
        #每个角色单独的战报记录 记录所有事件(动作，造成伤害，承受伤害) {时间:事件}
        #6人 暂不支持召唤物
    def __str__(self):
        return self.string
    def __repr__(self):
        return self.data
    
    def get_spell(self,champ,ls,team):
        ls.clear()
        spell = champ.genspell()
        self.string+=teams[team]+ champ.name+': '+spell[0]+'\n'
        time1, time2 = spell[1],spell[2]
        time1+= get_random_time()
        ls.enqueue([time1,spell])
        ls.enqueue([time2,None])    
        
    def cast_spell(self,champ,spell,team): #['甜蜜梦境',5,0,[1,300,5,(4,0.7)]]
        data = spell[-1]
        a = champ.a
        enemyteam = eval('self.t'+str(2-team))
        current,oppo = teams[team],teams[1-team]
        for i in range(len(data)):
            defender = []
            if i%3 == 0:
                if data[i] == 1:
                    try:
                        defender.append(enemyteam[data[i+1]])
                    except IndexError:
                        defender.append(enemyteam[0])
                if data[i] == 2:
                    defender = enemyteam
                if data[i] == 3:
                    times = data[i+1]
                    data_tmp = []
                    for i in range(len(data)):
                        data_tmp.append(data[i])                    
                    for i in range(times):
                        target = random.randint(0,2)
                        data_tmp[0],data_tmp[1] = 1, target
                        tmp = [spell[0],data_tmp]
                        self.cast_spell(champ,tmp,team)
            if len(defender) == 0:
                continue
            self.string += current+ champ.name+' 使用的 ' +spell[0]+'\n'
            for enemy in defender:
                damage = min(round(dmg(a,enemy.d,data[i+2]/100)),enemy.hp)
                self.string+= '对 '+ oppo +enemy.name+ ' 造成了 ' + str(damage)+ '的伤害'+'\n'
                change_state(enemy,3,-1*damage)
                self.string += oppo+ enemy.name + '剩余' +str(enemy.hp) +'/'+str(enemy.hp_limit) + 'hp\n'
                if enemy.hp == 0:
                    self.string += current +champ.name +'击杀了' +oppo +enemy.name+'\n'
                    '''
                    enemyteam[enemyteam.index(enemy)] = None
                    count = 0
                    for enemy in range(len(enemyteam)):
                        if enemy != None:
                            count +=1
                    if count == 0 :
                        raise
                    '''
                    enemyteam.remove(enemy)
                    if len(enemyteam)==0:
                        raise
            self.string +='\n'
    def get_attack(self,champ,ls):
        attack = champ.basic_attack
        time1, time2 = attack[1],attack[2]
        time1+= get_random_time()
        ls.enqueue([time1,attack])
        ls.enqueue([time2,None])                    
                        
    def run(self):
        #l*:每个角色即将发生的事件，可被打断 self.events:已出手的攻击，不可被取消
        #temp queue 记录每个角色即将发生的事件 [剩余时间,事件] 剩余时间循环 -1
        l1 = queue()
        l2 = queue()
        l3 = queue()
        l4 = queue()
        l5 = queue()
        l6 = queue()
        for i in range(0,1800):         #时间上限180秒，即30回合
            a = self.events.reduce_all()
            if a != None:
                for event in a:
                    tmp,champ,spell,count = event
                    
                    team = (count-1)//3
                    
                    self.cast_spell(champ,spell,team)
                    self.record(count,i/10,spell)            
            if i != 0 and i%60==0:      #能量条清空
                self.string+='\n'
                for champ in self.t1:
                    tmp = eval('l'+str(self.t1origin.index(champ)+1))
                    self.get_spell(champ,tmp,0)
                for champ in self.t2:                   
                    tmp = eval('l'+str(self.t2origin.index(champ)+4))
                    self.get_spell(champ,tmp,1)
            else:
                for champ in self.t1:                    
                    count = self.t1origin.index(champ)+1
                    tmp = eval('l'+str(count))
                    if tmp.isEmpty():
                        self.get_attack(champ,tmp)                
                    else:
                        a = tmp.reduce()
                        if a :
                            spell = a[1]
                            if spell:
                                self.events.enqueue([spell[2],champ,spell,count])
                                
                for champ in self.t2:             
                    count = self.t2origin.index(champ)+4
                    tmp = eval('l'+str(count))
                    if tmp.isEmpty():
                        self.get_attack(champ,tmp)
                    else:
                        a = tmp.reduce()
                        if a:
                            spell = a[1]
                            if spell:
                                self.events.enqueue([spell[2],champ,spell,count])

    def record(self,count,t,info):
        tmp = str(t)+'\t'
        for element in info:
            tmp += str(element)+' '
        tmp += '\n'
        exec( 'self.r'+str(count)+'+=tmp')
                    