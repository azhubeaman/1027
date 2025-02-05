#作者：Ourjune
#开发时间：2021/12/22 8:14
#动态绑定属性和方法

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')

stu1=Student('张三',20)
stu2=Student('李四',21)
stu1.eat()
stu2.eat()

#动态绑定  为stu2动态绑定性别属性
stu2.gender='女'
print(stu2.name,stu2.age,stu2.gender)
# print(stu2.name,stu2.age,stu1.gender)  stu1没有做绑定
print('----------------')

#动态绑定方法
def show():
    print('定义在类之外的，称为函数')
stu1.show=show
stu1.show()
#stu2.show() 没有绑定方法

