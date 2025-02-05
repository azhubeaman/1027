#作者：Ourjune
#开发时间：2021/10/27 8:43
#数据类型 整数类型型、浮点型、布尔型、字符串类型（int\float\bool\str）

#整型 正数、负数、0
#默认十进制
n1=11
n2=-11
n3=0
print(n1,type(n1))
print('十进制',101) #取值范围0~9
print('二进制',0b010101)#二进制 0b  取值范围0、1
print('八进制',0o176)#八进制 0o   数字范围是0~7
print('十六进制',0x1AF)#十六进制0x  大小写X不区分 数字范围0~9和A~F

#浮点类型
a=3.1415926
print(a,type(a))
#浮点数存储具有不准确性（二进制底层问题，不需要深究）
n1=1.1
n2=2.2
n3=2.1
print(n1+n2)
print(n1+n3)
#解决方案
#导入模块decimal
from decimal import  Decimal
print(Decimal('1.1')+Decimal('2.2'))

#布尔类型
#用来表示真或者假的值
f1=True
f2=False
print(f1,type(f1))
print(f2,type(f2))
#布尔值可以转化为整数 True表示1 false表示0
print(f1+1) #2
print(f2+1) #1

#字符串类型
#字符串成为不可变的字符序列
#使用单，双，三引号，或'''   '''
str1='今天好困，我学python'
print(str1,type(str1))
str2="今天好困，我学python"
print(str2,type(str2))
#三引号可以分行写
str3="""今天好困，
我学python"""
str4='''今天好困，
我学python'''
print(str3,type(str3))
print(str4,type(str4))