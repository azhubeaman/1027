#作者：Ourjune
#开发时间：2021/12/13 15:55
#斐波那契数列
#1 1 2 3 5 8 13 ···第三项开始为前两项之和

def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        res=fib(n-2)+fib(n-1)
        return res
print(fib(6)) #斐波那契数列第六位上的数字是

#输出这个数列的前六位上的数字
print('------------')
for i in range(1,7):
    print(fib(i),end='\t')