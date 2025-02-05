#作者：Ourjune
#开发时间：2021/10/30 8:18
#for-in 循环   for 自定义的变量  in 可迭代的对象

#for item in 'python': #第一次取出来的是p，将p赋值给item，将item的值输出...
#   print(item)

#range()产生整数序列，也是可迭代对象
for i in range(2,11,2):
    print(i)

#如果在循环体中，不需要使用到自定义变量，可将自定义变量写为‘_’
for _ in range(5):
    print('------')  #‘-------’循环输出五次

print('使用for循环计算1-100偶数和')
sum=0
k=0
for k in range(2,101,2):
    sum+=k
print('和为',sum)