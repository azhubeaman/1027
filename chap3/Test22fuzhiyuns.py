#作者：Ourjune
#开发时间：2021/10/28 8:34
#赋值运算符

#赋值运算符，运算顺序从右到左
#支持链式赋值
i=3+4
print(i)
a=b=c=20  #链式赋值
print(a,id(a))
print(b,id(b))
print(c,id(c))#abc id一样，指向同一个地址
print('-----------------支持参数赋值----------------')
a+=30 #相当于a=a+30
print(a)
a-=10 #相当于a=a-10
print(a)
a*=2  #相当于a=a*2
print(a)
a/=3
print(a)#a从这里开始变为float类型了
a//=2
print(a)
a%=3
print(a)

#支持系列解包赋值
print('--------解包赋值-----------')
a,b,c=20,30,40
print(a,b,c)
print('------交换两个变量的值---------')
a,b,c=b,c,a
print('交换之后：',a,b,c)