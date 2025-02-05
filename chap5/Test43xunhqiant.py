#作者：Ourjune
#开发时间：2021/11/2 7:57
#嵌套循环

#题目要求：输出一个三行四列的矩形
'''for i in range(1,4): #行，执行三次
    for j in range(1,5):
        print('*',end='\t') #不换行输出
    print() #换行'''

#打印一个直角三角形
'''*
   **
   ***
   ****
   *****
   ******
   *******
   ********
   *********'''
for i in range(1,10):
    for j in range(1,i+1):
        print('*',end='')
    print()

#九九乘法表：
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()