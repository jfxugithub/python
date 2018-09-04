
import gun

class People:

    def __init__(self, name):
        self.name = name
        self.blood = 100
        self.gun = gun.Gun()

    def take_gun(self):
        self.gun.gun_statu = gun.GUNTAKE
        print("拿起枪")

    def put_gun(self):
        self.gun.gun_statu = gun.GUNPUT
        print("放下了枪")

    #将敌人杀死返回True否则返回False
    def shoot_enemy(self,enemy):
        print("%s想要射击%s" % (self.name,enemy.name))

        #判断枪是否被拿起来,拿起来后这轮不能开枪
        if not self.gun.gun_statu:
            self.take_gun()
            return False

        if self.gun.shoot_bullet(self,enemy):
            #射杀一人需要放下枪
            self.put_gun()
            return True
        else:
            return False
