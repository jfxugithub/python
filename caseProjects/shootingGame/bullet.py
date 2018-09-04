"""
子弹威力随机
"""
import random
# import people

class Bullet:

    def hurt_enemy(self,enemy):
        power = random.randint(0,10)
        print("子弹威力%s,%s血量%s" % (power,enemy.name,enemy.blood))
        enemy.blood -= power
        if enemy.blood > 0:
            print("%s还有血量为:%d" % (enemy.name,enemy.blood))
            return False
        else:
            print("%s被你击毙了" % (enemy.name))
            return True
