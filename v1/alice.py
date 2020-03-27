import random
class alice():
    def __init__(self, attack, defense, hp0, sup = None):
        self.name = '爱丽丝'
        self.a = attack
        self.d = defense
        self.hp_limit = hp0
        self.hp = hp0
        self.sup = sup
        self.dodge = 0          #闪避未实装
        self.spell_list = [['甜蜜梦境',20,10,[1,300,5,(4,0.7)]],  #甜蜜梦境 前摇2s，后摇1s。对单体造成300%倍率伤害，增加辅助目标70%闪避
                           ['蒂奇!',20,10,[2,150,8,(2,1)]]]
                           #['梦魇',20,10,[1,300,5,(4,1)]]]
        self.basic_attack=['普通攻击',20,10,[1,100]]

        ##蒂奇 梦魇未实装
        #技能名 前摇 后摇 效果1 目标 ... 效果2(if exists) 目标 3....
        #target type1: 1:敌单体 2:敌全体 3:随机n段数(3,n)
        #target type2(辅助): 4:效果1生效目标 5:辅助目标 6:己方全体 7:自身 8:前排
        #......
        #辅助特效：1 (攻击,值)2(防御,%)3(治疗,值)4(闪避,%)

    def genspell(self):         #摇技能
        return random.choice(self.spell_list)



    
        

