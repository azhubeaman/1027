#作者：Ourjune
#开发时间：2021/12/23 7:56

class Person:
    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的is为{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建的对象的id为：{0}'.format(id(obj)))
        return obj
    def __init__(self,name,age):
        print('__init__被调用了，self的id值为{0}'.format(id(self)))
        self.name=name
        self.age=age
print('object这个类对象的id为{0}'.format(id(object)))
print('Person这个类对象的id为{0}'.format(id(Person)))

#创建Person类的实例对象
p1=Person('张三',20)
print('p1这个Person类的实例对象id为{0}'.format(id(p1)))