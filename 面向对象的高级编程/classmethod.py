"""
类方法:
    类所拥有的方法，需要使用到修饰器 @classmethod
    对于类方法，第一个参数必须是类对象，一般以cls表示作为第一个参数(当然可以用其他的名字，但是不建议修改）

作用:
    类方法可以对类属性进行修改,而不会避免了实例属性的创建
发现规律:
    结果显示在用类方法对类属性进行操作修改之后,通过类对象和实例对象访问都发生了变化

"""
class Student:
    school = "太阳系学院"

    @classmethod
    def getSchool(cls):
        return cls.school

    @classmethod
    def setSchool(cls,school):
        cls.school = school


stu = Student()
print(stu.school)
print(stu.getSchool())
print(Student.school)
print(Student.getSchool())

print("-"*35)
stu.setSchool("银河系学院")
print(stu.school)
print(stu.getSchool())
print(Student.school)
print(Student.getSchool())
print("-"*35)