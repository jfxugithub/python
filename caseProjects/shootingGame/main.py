import random

from people import People

def app():

    laoLiu = People("老刘")
    laoWan = People("老王")
    laoLin = People("老林")

    peopleList = [laoLiu, laoWan, laoLin]
    nu = 1  # 记录回合数

    """随机获取一名要敌人"""
    def get_enemy(gunerName):
        while True:
            enemy = random.choice(peopleList)
            if enemy.name != gunerName:
                return enemy

    #每个人开一枪,看谁活到最后
    while True:
        print("=" * 10 + ("第%d回合" % nu) + "=" * 10)

        if laoWan.blood > 0:
            print("%s:" % laoWan.name)
            enemy = get_enemy(laoWan.name)
            if laoWan.shoot_enemy(enemy):
                peopleList.remove(enemy)

        if laoLiu.blood > 0:
            print("%s:" % laoLiu.name)
            enemy = get_enemy(laoLiu.name)
            if laoLiu.shoot_enemy(enemy):
                peopleList.remove(enemy)

        if laoLin.blood > 0:
            print("%s:" % laoLin.name)
            enemy = get_enemy(laoLin.name)
            if laoLin.shoot_enemy(enemy):
                peopleList.remove(enemy)

        if len(peopleList) == 1:
            print("最终的赢家是:", peopleList[0].name)
            break

        nu += 1


app()
