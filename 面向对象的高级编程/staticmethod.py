"""
静态方法定义:
    通过修饰器staticmethod来进行修饰,不需要传参数
    加载时机:随着类的加载而加载
实例方法:
    加载时机:随着对象的加载而加载
"""


class Student:

    address = "太阳系"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod             #修饰静态方法
    def get_address():
        return Student.address



print(Student.get_address()) #不需要声明对象而直接调用方法
