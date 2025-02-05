#作者：Ourjune
#开发时间：2021/12/23 8:10

#变量的赋值操作，只是形成两个变量，实际上还是指向同一个对象
class Cpu:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
#变量的赋值
c1=Cpu()
c2=c1
print(id(c1),id(c2))

#浅拷贝,只拷贝原对象，子对象不拷贝
print('---------------------')
d1=Disk()  #创建Disk类的对象
computer=Computer(c1,d1)#创建Computer类的对象
import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)#computer的两个子对象
print(computer2,computer2.cpu,computer2.disk)#computer2的两个子对象

#深拷贝,递归拷贝对象中
print('--------------------')
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)

