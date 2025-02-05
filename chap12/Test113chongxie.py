#作者：Ourjune
#开发时间：2021/12/22 19:14

#作者：Ourjune
#开发时间：2021/12/22 18:51
#继承

'''
class 子类类名（父类1，父类2...）:  py支持多继承
    pass
'''
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
    def info(self):     #重写
        super().info()
        print(self.stu_no)

class Teather(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear
    def info(self):     #重写
        super().info()
        print(self.teachofyear)

stu=Student('张三',18,1)
teacher=Teather('李四',28,5)

stu.info()
print('--------------')
teacher.info()