global combo_list,dot,cons_buff,pros_buff,direct_dmg
dot = []                                                          #异常状态伤害
cons_buff = [(3,21,12),(3,23,12),(3,21),(3,23),(21,12),(22,12)]   #削弱，控制，异常状态
pros_buff = []                                                    #己方增益
direct_dmg = [(3,21,11),(3,23,11),(21,11),(22,11)]                #直接伤害
combo_list = dot+cons_buff+pros_buff+direct_dmg


def include(l1,l2):         #determine if l1 is included in l2
    include = True
    for spell in l1:
        if spell not in l2:
            include = False
    return include
    
def find_outliner(l1,l2):   #find elments in l1 which is not in l2
    outliner = []
    for spell in l1:
        if spell not in l2:
            outliner.append(spell)
    return outliner
def determine_combo(spell_list):
    for i in range(len(combo_list)):
        if include(combo_list[i],spell_list):
            return combo_list[i]
    return []


def get_combo_type(combo):
    if combo in dot:
        return '异常状态伤害'
    if combo in cons_buff:
        return '敌方削弱'
    if combo in pros_buff:
        return '己方增益'
    if combo in direct_dmg:
        return '大量伤害'
    return ''
'''
boo, combo = determine_combo([1,12,22])
print(get_combo_type(combo))
'''