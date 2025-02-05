#作者：Ourjune
#开发时间：2021/11/2 7:44
#if..else..   不满足if就执行else
#while...else
#for..else    后两个碰到break就不执行else

'''for item in range(3):
    pwd=input('请输入密码')
    if pwd=='888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print('对不起，三次密码均输入错误')'''

#使用while
a=0
while a<3:
    pwd=input('请输入密码')
    if pwd=='999':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a+=1
else:
    print('对不起，三次密码都失败了')
