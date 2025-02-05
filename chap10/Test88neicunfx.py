#作者：Ourjune
#开发时间：2021/12/8 8:05
#函数的参数传递的内存分析
def fun(str1,str2):
    print('str1',str1)
    print('str2',str2)
    str1=100
    str2.append(10)
    print('str1',str1)
    print('str2',str2)

n1=11
n2=[11,22,33]
print('n1',n1)
print('n2',n2)
fun(n1,n2)  #将位置传参，str1,str2是函数定义处的形参，n1,n2是函数调用处的实参。总结：实参名称和形参名称可以不一致
print('n1',n1)
print('n2',n2)

#如果是不可变对象，在函数体内的修改不会影响实参的值 str1的修改
#如果是可变对象，在函数体内的修改会影响到实际的值  str2的修改会影响n2的值