#作者：Ourjune
#开发时间：2021/12/8 8:27
#函数的参数定义
def fun(a,b=10):  #b的默认值参数为10
    print(a,b)

fun(100)
fun(20,30)
#当实参与形参默认值不一致的时候才会替换

print() #print函数也有默认值，end=\n
print('======================')
#个数可变的位置参数
#定义参数时，可能无法事先确定传递 位置 实参的个数时，使用可变的位置参数
def fun1(*args):  #函数定义时的    可变的位置参数
    print(args)
    #print(args[0])
fun1(10)
fun1(10,30)
fun1(120,312,123)
print('输出结果为元组')
#个数可变的关键字形参
#定义函数时，无法事先确定传递的 关键字 实参的个数时，使用可变的关键字形参
def fun2(**args):
    print(args)
fun2(a=11)
fun2(a=12,b=21,c=33)
print('输出结果为字典')

'''def fun3(*args,*a):  #同理**args,**a也会报错
    pass
    以上代码，程序会报错，个数可变的 位置和关键字 参数只能有一个
'''
def fun4(*args,**args2):
    pass
'''def fun5(**args,*args2):
    pass
    在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，要求个数可变的位置形参放在前面，否则会报错
    '''