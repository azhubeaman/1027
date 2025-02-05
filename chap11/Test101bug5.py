#作者：Ourjune
#开发时间：2021/12/21 8:24

#在不知道会报什么错的情况下，
#可以用try...except...else
#可以用try...except...else...finally  不论结果是什么都会执行，能常用来释放try块中申请的资源
'''try:
    a = int(input('第一个整数'))
    b = int(input('请输入第二个整数'))
except BaseException as e:
    print('出错了',e)
else:
    res = a / b'''

try:
    a = int(input('第一个整数'))
    b = int(input('请输入第二个整数'))
except BaseException as e:
    print('出错了',e)
else:
    res = a / b
    print('计算结果为：',res)
finally:
    print('谢谢你的使用')
print('程序结束')