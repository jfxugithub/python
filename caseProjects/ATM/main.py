import atm

from caseProjects.ATM.atm import AutomaticTellerMachine

atm_ = AutomaticTellerMachine()

def app():
    print("*" * 20 + "欢迎使用ATM" + "*" * 20)
    while True:
        print("您可以进行以下操作:")
        print("\t1.存钱; 2.取钱; 3.显示余额; 4.退出")

        selection = int(input("请输入你需要的选项:"))
        if selection not in [1, 2, 3, 4]:
            print("***您输入的选项有误,请重写输入")
            print("*" * 50)
            continue

        if selection is 1:
            money = int(input("请将纸币放入ATM存钱口:"))
            atm_.save_money(money)

        elif selection is 2:
            print("您的余额还有:%f" % atm_.show_money())
            money = int(input("请输入您需要提取的金额:"))
            atm_.get_money(money)

        elif selection is 3:
            print("您的余额还有:%f" % atm_.show_money())

        else:
            print("*" * 20 + "感谢您的使用" + "*" * 20)
            break
        print("*" * 50)


app()
