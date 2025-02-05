#作者：Ourjune
#开发时间：2021/10/28 8:12

#输入函数input
#present=input('你想要什么生日礼物呢？')
#print(present,type(present))

#练习题：从键盘录入2个整数，计算两个整数的和
#方法一
#a=input('请输入一个加数')
#b=input('请输入另一个加数')
#print(a+b) #input输出的是str类型，需要转换，否则+起到拼接作用，不是相加功能
#print(int(a)+int(b))
#方法二
#直接在输入的时候转换
a=int(input('请输入一个加数'))
b=int(input('请输入另一个加数'))
print(a+b)