#作者：Ourjune
#开发时间：2021/11/2 7:37
#continue用于结束当前循环，开始下一次循环

#题目要求：要求输出1-50之间所有5的倍数 5，10，15，20...
#5的倍数共同点：和5的余数为0的数都是5的倍数

'''for i in range(1,51):
    if i%5==0:
        print(i)'''
print('----------使用continue---------')
for i in range(1,51):
    if i%5!=0:
        continue
    else:
        print(i)