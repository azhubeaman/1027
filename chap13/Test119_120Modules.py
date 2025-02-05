#作者：Ourjune
#开发时间：2021/12/23 8:41
#模块
#一个模块中可以包含N多个函数；一个.Py文件就是模块

#导入模块
import math  #关于数学运算的模块
print(id(math))
print(type(math))
print(math)
print('----------------')
print(dir(math))
print(math.pi)  #Π
print(math.pow(2,3),type(math.pow(2,3))) #2的三次方
print(math.ceil(9.0001))  #向上取整
print(math.floor(9.9999)) #向下取整
print('----------------')
#导入模块（2）
'''from math import pi
print(pi)
print(pow(2,3))
#print(math.pow(2,3))  #报错，因为只导入了pi
'''