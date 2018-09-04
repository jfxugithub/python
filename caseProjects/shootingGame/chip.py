
"""
    初始子弹数随机

"""
import random

from bullet import Bullet

CHIPVOLUME=10

class Chip:

    def __init__(self, bullet_nu=0, chip_volume=CHIPVOLUME):
        self.chip_volume = chip_volume
        if bullet_nu == 0:
            self.bullet_nu = random.randint(1,10)
        else:
            self.bullet_nu = bullet_nu
        self.bullet = Bullet()

    def add_bullet(self,num):
        if (self.bullet_nu + num) > self.chip_volume:
            self.bullet_nu = self.chip_volume
            print("只能安装%d颗子弹,已装满" %  self.chip_volume)
        else:
            self.bullet_nu += num
            print("已安装%d颗子弹,弹夹一个有%d颗子弹" % ( num, self.bullet_nu))

    def sub_bullet(self):
        if self.bullet_nu == 0:
            print("没有子弹了,无法射杀敌人")
            return False

        self.bullet_nu -= 1
        return True
