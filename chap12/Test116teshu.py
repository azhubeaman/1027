#作者：Ourjune
#开发时间：2021/12/22 19:45

#特殊属性：__dict__

#特殊方法：__
a=20
b=100
c=a+b  #两个整数类型的对象的相加操作
d=a.__add__(b)  #上述底层操作
print(c)
print(d)
print('---------------')

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)
stu1=Student('张三')
stu2=Student('李四')
s=stu1+stu2    #未写add方法，会报错
print(s)
print('---------------')
lst=[11,22,33,44]
print(len(lst))
print(lst.__len__())  #内置函数，计算长度
print('---------------')
print(len(stu1))  #和add方法一样，需要写len方法