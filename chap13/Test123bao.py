#作者：Ourjune
#开发时间：2021/12/24 8:21
#python中的包
#包和文件的区别，包中自带init.py
#包中包含模块
'''
注意：使用import方式进行导入时，只能跟包名或者模块名
     使用from 方式进行导入时，可以导入包，模块，或者函数，变量
'''

#import方式导入只能跟包名或者模块名
import pageage1
import pageage1.ModuleA as ma  #ma是别名
print(ma.a)

#使用from方式导入可以导入包，模块，或者函数，变量
from pageage1 import  ModuleB
from pageage1.ModuleB import b
print(b)