"""
动态创建类:
    type(类名,父类集合,属性字典)
    类名:动态创建类的名字
    父类集合:创建的类所要继承的父类set集合,可以为空
    属性字典:创建属性,已字典的形式入参
"""


"""=====================添加属性====================="""
People = type("People", (), {"name": "小东", "sex": "woman"})
peo = People()
print(peo.name, ":", peo.sex)

"""=====================添加继承====================="""
Teacher = type("Teacher", (People,), {"work": "EnglishTeacher"})
teacher = Teacher()
teacher.name = "TeacherHuang"
teacher.set = "man"
print(teacher.name,"work:",teacher.work)

"""======================添加函数====================="""
@classmethod
def show(cls):
    print("this is classmethod :show")

@staticmethod
def sshow():
    print("this is  staticmethod :sshow ")


#添加类方法和静态方法
Class_01 = type("Class_01",(),{"show":show,"sshow":sshow})
Class_01.show()
Class_01.sshow()

