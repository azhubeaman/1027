#作者：Ourjune
#开发时间：2021/12/13 14:30
#变量的作用域

def fun(a,b):
    c=a+b  #c是局部变量，因为是在函数体内；ab作为函数的形参，作用范围也是函数内部，所以相当于局部变量
    print(c)
#print(c)  报错
#print(a)  报错  因为ac超出了作用域

name='烦老师'
def fun1():
    print(name)
fun1()
print(name) #name是全局变量，所以函数外也能输出

print('-----------')
def fun2():
    global age   #这里定义了全局变量（局部变量使用global声明）
    age=20
    print(age)
fun2()
print(age)       #所以这边不会报错
