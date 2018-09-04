"""
添加子弹个数随机
"""
import random
# import people
from chip import CHIPVOLUME
from chip import Chip

GUNPUT = False
GUNTAKE = True

class Gun:
    def __init__(self):
        self.chip = Chip()
        self.gun_statu = GUNPUT

    # 装弹夹
    def load_chip(self):
        print("弹夹安装完毕")

    # 射击
    def shoot_bullet(self,guner,enemy):
        if self.chip.sub_bullet():
            print("成功射击%s" % enemy.name)
            if self.chip.bullet.hurt_enemy(enemy):
                return True
            else:
                return False
        else:
            guner.put_gun()
            self.chip.add_bullet(random.randint(1, CHIPVOLUME))
            self.load_chip()
            return False

