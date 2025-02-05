#作者：Ourjune
#开发时间：2021/10/29 7:19
#比较运算符
#结果是bool类型 > < >= <= == !=

'''一个 = 称为赋值运算符 ， ==称为比较运算符
  一个变量由三部分组成，标识，类型，值
  == 比较的是值还是标识呢？ 比较的是值
  比较对象的标识使用 is'''

a=10
b=10
print(a==b) #True 说明，a与b的value，相等
print(a is b)#True 说明，a与b的id标识，相等
#以下代码没学过，后面会讲解
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)
print(lst1 is lst2)#false 因为id不等
print(lst1 is not lst2)#true

