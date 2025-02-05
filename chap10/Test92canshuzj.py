#作者：Ourjune
#开发时间：2021/12/13 13:47
#参数总结
def fun(a,b,c): #a,b,c在函数的定义处，所以是形式参数
    print('a=',a)
    print('b=',b)
    print('c=',c)
fun(10,20,30) #函数调用时的参数传递，称为位置传参
print('---------------')
lst=[12,13,14]
#fun(lst)  会报错
fun(*lst) #在函数调用时，将列表中的每个元素都转换为位置实参传入

fun(a=100,b=101,c=102)#函数的调用，所以是关键字实参
print('--------------')
dic={'a':111,'b':222,'c':333}
fun(**dic)  #函数调用时，将字典中的键值对都转换为关键字实参进行传入
print('------------')


def fun1(a,b,*,c,d):   #从*之后的参数，在函数调用时，只能采用关键字参数传递
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=',d)
# fun1(10,20,30,40)     报错
fun1(10,20,c=30,d=40)
print('------------')
#函数定义是的形参的顺序问题
def fun2(a,b,*,c,d,**args):
    print(a,b,c,d,args)
fun2(10,20,c=1,d=2,e=11)

def fun3(*args,**args2):
    print(args,args2)
fun3(10,b=100,c=222)

def fun4(a=10,b=20,*args,**args2):
    pass
