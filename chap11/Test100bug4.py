#作者：Ourjune
#开发时间：2021/12/21 8:12
#被动掉坑：程序代码逻辑没有错，只是因为用户错误操作或者一些例外情况而导致的程序崩溃
#题目要求：输入两个整数并进行除法运算
'''
a=int(input('第一个整数'))
b=int(input('请输入第二个整数'))
res=a/b
print('结果为:',res)
'''

#python异常处理机制
try:
    a = int(input('第一个整数'))
    b = int(input('请输入第二个整数'))
    res = a / b
    print('结果为:', res)
except ZeroDivisionError:  #不允许被0除的异常
    print('除数不能为0哦')
except ValueError:
    print('只能输入数字串')
print('程序结束')