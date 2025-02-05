#作者：Ourjune
#开发时间：2021/12/22 7:57

class Student:
    native_place='浙江'   #类属性
    def __init__(self,name,age):
        self.name=name  #self.name 称为实体属性，进行了一个赋值的操作，将局部变量name的值赋值给实体属性
        self.age=age
    #实例方法
    def eat(self):
        print('学生在吃饭...')
    #静态方法
    @staticmethod
    def method():   #静态方法里不能写self
        print('我使用了静态方法')
    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了类方法')

def drink():
    print('喝水')

#创建Student类的对象
stu1=Student('张三',20)   #stu1是类对象创建出来的实例对象

stu1.eat()   #对象名.方法名()
print(stu1.name)
print('-------------')
Student.eat(stu1)  #30行与27行功能相同
                   #类名.方法名(类的对象)-->实际上就是方法定义的self