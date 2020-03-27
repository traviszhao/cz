test1 
蓝色方(左手) 为攻 防 血量 为 10000,5000,200000的爱丽丝，技能只有12，只有伤害无特效
紫色方为(8000,4000,100000)的爱丽丝
伤害公式 dmg = a**2/(a+d)，上下浮动3%

v0： 无组合技,无dot 无护盾 无被动 无增减伤 无阶段 无攻击距离
英雄
init
attack0 面板攻击
*attack1 实际攻击
defense
hp_limit
hp
*spelllist
sup: default = none
*attack speed: default = 3
dodge = 0 闪避

def take dmg(source,effect)
    hp 削减
def heal(amount, effect)
    hp ++
def get attack(self)
   return attack 1
*普通攻击初始为 1.0加成 目标单体 无特效 2秒前摇1秒后摇的技能
spell 
   t1(固定前摇)
  t2(固定后摇)
  effect (加成)
  target1(目标)
  special-effect1(特效)
  target2(辅助目标)
  se2(辅助特效)



fight 
dmg = a^2/(a+d)
**时间轴
根据时间轴产生事件，6秒/60单位为一回合，回合结束后强制终止任何进行中的事件
每个事件随机0-0.5秒/5单位的随机前摇 以免同归于尽
generate random spell range(0,3)

bqueue: [tuple](事件,time)









判定冰冻 承伤方受到寒冷且受到来源相同的技能伤害
冰妈3技能 敌方全体各n//a段,(n为总段数,3+被动层数//2)，n%a段再随机
test：
双方 team init 为 william(16w.....) alice(20w.... sup = william) elwing(244700....)