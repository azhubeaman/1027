#作者：Ourjune
#开发时间：2021/11/2 8:16
#二重循环
#二重循环中的break和continue只控制本层循环

'''for i in range(5):
    for j in range(1,11):
        if j%2==0:
            break
        print(j)'''
'''内层循环只执行了一次，外层循环执行了5次，所以打印出了5行1'''
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()