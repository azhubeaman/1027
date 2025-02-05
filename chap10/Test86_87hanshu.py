#作者：Ourjune
#开发时间：2021/12/8 7:47
#函数的创建和调用
#参数传递
def calc(a,b):#a,b称为形式参数，形参的位置是在函数的定义处
    c=a+b
    return c
result=calc(1,2)#1，2称为实际参数的值，实参的位置是函数的调用处  按位置传参
print(result)

res=calc(b=1,a=2)#传递的方式和上面不一样，这是关键字传参
print(res)