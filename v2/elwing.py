import random
class elwing():
    def __init__(self, attack, defense, hp0, sup = None):
        self.name = '艾尔薇'
        self.a = attack
        self.d = defense
        self.hp_limit = hp0
        self.hp = hp0
        self.sup = sup
        self.dodge = 0          #闪避未实装
        self.spell_list = [['星落',20,10,[1,0,450]],  
                           ['碎星箭',20,10,[1,0,450]],
                           ['流星',20,10,[3,4,170,4,5,-35]]]
        self.basic_attack=['普通攻击',20,10,[1,0,100]]

        
        #技能名 前摇 后摇 效果1 目标 ... 效果2(if exists) 目标 3....
        #target type1: 1:敌单体 2:敌全体 3:随机n段数(3,n)
        #target type2(辅助): 4:效果1生效目标 5:辅助目标 6:己方全体 7:自身 8:前排
        #......
        #辅助特效：1 (攻击,值)2(防御,%)3(治疗,值)4(闪避,%)5治疗百分比%

    def genspell(self):         #摇技能
        return random.choice(self.spell_list)



    
        

