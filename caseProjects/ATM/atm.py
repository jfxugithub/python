"""
atm业务:
1.存钱
2.取钱
3.查询余额


Automatic Teller Machine
"""


class AutomaticTellerMachine:
    def __init__(self):
        self.__balance = 0.0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, money):
        if (money % 100) is 0:
            self.__balance += money
            if money > 0:
                print("您成功存入%d元" % money)
            else:
                print("您成功取出%d元" % (-1*money))

    def save_money(self, money):
        if money % 100 is 0 and money > 0:
            self.balance = money
        else:
            print("存入的金额必须是百元纸币,请至少放入一张百元纸币")

    def get_money(self, money):
        if money > self.balance:
            print("目前账户余额只有:%f元,无法取出%f元" % (self.balance, money))
            return
        self.balance = -1 * money

    def show_money(self):
        return self.balance
