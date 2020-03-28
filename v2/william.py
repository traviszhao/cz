import random
class william():
    def __init__(self, basic_attack, attack_ratio,defense,defense_ratio, hp0, index = 0):
        self.name = '威廉·姆斯兰'
        self.ar = attack_ratio
        self.a = basic_attack*self.ar
        self.dr = defense_ratio
        self.d = defense*self.dr
        self.hp_limit = hp0
        self.hp = hp0
        self.sup = None
        self.dodge = 0          #闪避未实装
        self.spell_list = [['冰封之铠',15,10,[1,0,450,7,2,500,9,2,33]],  
                           ['水晶之刃',15,10,[1,0,450,4,2,33]],
                           ['凛冬已至',15,10,[2,None,225]]]
        self.basic_attack=['普通攻击',15,10,[1,0,100]]
        self.index = index
        self.rang = 175
        #技能名 前摇 后摇 效果1 目标 ... 效果2(if exists) 目标 3....
        #target type1: 1:敌单体 2:敌全体 3:随机n段数(3,n)
        #target type2(辅助): 4:效果1生效目标 5:辅助目标 6:己方全体 7:自身 8:前排 9敌全体
        #......
        #辅助特效：1 (攻击,值)2(防御,%)3(治疗,值)4(闪避,%)5治疗百分比%

    def genspell(self):         #摇技能
        return random.choice(self.spell_list)



    
        

