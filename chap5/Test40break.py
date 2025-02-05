#作者：Ourjune
#开发时间：2021/11/2 7:22
#从键盘录入密码，最多录入三次，正确就结束循环

'''for i in range(3):
    pwd=int(input('请输入密码'))
    if pwd==999:
        print('密码正确')
        break
    else:
        print('密码不正确')'''

#用while实现
i=0 #定义变量
while i<3:
    #条件执行体
    pwd=input('请输入密码')
    if pwd=='999':
        print('密码正确')
        break
    else:
        print('密码不正确')
    #改变变量
    i+=1