#作者：Ourjune
#开发时间：2021/12/22 7:40
#类与对象
#类是多个类似事物组成的群体的统称。能够帮助我们快速理解和判断事务的性质

'''
class Student:  #Student为类的名称（类名）由一个或多个单词组成，每个单词的首字母大写，其余小写
    pass

#一切皆对象
print(type(Student))  #<class 'type'>
print(id(Student))  #2555996405624
print(Student)  #<class '__main__.Student'>
'''

#类的组成
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

#在类之外定义的称为函数，在类之内定义的称为方法
def drink():
    print('喝水')