#作者：Ourjune
#开发时间：2021/12/22 8:05
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
    def method():   #静态方法里不能写self,无参数
        print('我使用了静态方法')
    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了类方法')

#类属性的使用方式
print(Student.native_place)
stu1=Student('张三',20)
stu2=Student('李四',21)
print(stu1.native_place)
Student.native_place='北京'  #stu1 stu2的类指针指向了类对象中的native_place地址，所以地址改变后，stu1,2指向也改变了
print(stu1.native_place)
print('--------------类方法的使用方式--------------')
Student.cm()
print('--------------静态方法的使用方式--------------')
Student.method()
