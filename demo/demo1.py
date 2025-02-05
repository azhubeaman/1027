#作者：Ourjune
#开发时间：2022/1/10 18:52
'''
with open('F:\\PYfile\\1027\studentsys\\test.txt','w',encoding='utf-8')as file:
    file.write('你好明天')
'''
'''
height=170
weight=50.6
bmi=weight/(height+weight)
print('你的身高是:',height)
print('你的体重是：',weight)
print('BMI:{:0.2f}'.format(bmi))
'''
'''def fun():
    num=int(input('请输入一个十进制的整数：'))#11
    print(str(num)+'的二进制数为'+bin(num))
    print('%s的十六进制数为%s'%(num,hex(num)))
    print('{0}的八进制数为{1}'.format(num,oct(num)))

if __name__ == '__main__':
    while True:
        try:
            fun()
            break
        except:
            print('只能输入整数，请重新输入')
            fun()'''

'''pwd=input('请输入支付密码')
if pwd.isdigit():   #用于判断输入的是否是数字
    print('支付密码合法')
else:
    print('支付密码不合法')'''

'''user=input('请输入用户名')
pwd=input('请输入密码')
passwd='123'
if passwd==pwd and user=='1165360167':
    print('登录成功')
else:
    print('对不起账号或者密码不正确')'''

'''
import random
price=random.randint(1000,1009)
print('今日竞猜商品为小米扫地机器人：价格在【1000-1009】之间')
def fun():
    if guess>price:
        print('大了')
    elif guess<price:
        print('小了')
    else:
        print('猜对了')
        print('真实价格为：',price)
if __name__ == '__main__':
    while True:
        try:
            guess = int(input())
            fun()
            if guess==price:
                break
        except:
            print('请输入整数')
'''

'''
x=97
for item in range(25):
    print(chr(x),'--->',x)   #chr()函数 返回值是当前整数对应的 ASCII 字符。
    x=x+1
'''

'''
def fun():
    if user == 'admin' and pwd == '8888':
        print('登陆成功')
    else:
        print('输入用户名或者密码错误！')
        if i!=0:
            print(f'你还有{i}次机会！')
        else:
            print('3次机会已使用完，请联系管理员！！')

if __name__ == '__main__':
    i = 2
    while i>=0:
        user=input('请输入用户名')
        pwd=input('请输入密码')
        fun()
        if user == 'admin' and pwd == '8888':
            break
        i = i - 1
'''

'''
def fun1():
    i=2
    while i>=0:
        user = input('请输入用户名')
        pwd = input('请输入密码')
        if user == 'admin' and pwd == '8888':
            print('登陆成功')
            break
        else:
            print('输入用户名或者密码错误！')
            if i != 0:
                print(f'你还有{i}次机会！')
                i=i-1
            else:
                print('3次机会已使用完，请联系管理员！！')
                break

if __name__ == '__main__':
    fun1()
'''
'''
import random
tnum=random.randint(1,100)
def fun():
    for i in range(1,100):
        num=int(input('我在心中有个1-100之间的数，请你猜一猜：'))
        if num<tnum:
            print('小了')
        elif num>tnum:
            print('大了')
        else:
            print('恭喜你猜对了')
            print(f'您一共猜了{i}次')
            break
    if i<4:
        print('真牛!!')
    elif i>=4 and i<=7:
        print('还凑合！')
    else:
        print('看来你得学一学二分法了！')
if __name__ == '__main__':
    fun()
'''

'''水仙花数
for i in range(100,1000):
    bw=i//100
    sw=i//10%10
    gw=i%10
    if bw*bw*bw+sw*sw*sw+gw*gw*gw==i:  #优化一下：导入math包，math.pow((i%10),3)=gw*gw*gw
        print(i)
'''

'''千年虫
year=[89,82,85,86,00,88,97]
print('原列表：',year)
for i,value in enumerate(year):
    #print(i,value)
    if value!=0:
        year[i]=int(str(19)+str(value))
    else:
        year[i]=int(str(200)+str(value))
print('修改后的列表：',year)
year.sort()
print('排序后的列表：',year)'''


#用递归把字符串倒序输出
'''str='hel'
def fun1():
    n = -1
    if len(str)==1:
        return str
    elif n<-len(str):
        return 1
    else:
        res=str[n:n+1]+fun1(n-1)
        return res
print(fun1(str))'''
'''
str='hel'
def fun1(str):
    if len(str)!=1:
        fun1(str[1:])
    print(str[0],end='')
fun1(str)'''

'''
#商品入库
lst=[]
for i in range(0,5):
    add=input('请输入你需要入库的商品：\n')
    lst.append(add)
for i in lst:
    print(i)

gift=[]
while True:
    num=input('请输入你需要购买的商品编号：')
    for i in lst:
        if i.find(num)!=-1:
            gift.append(i)
            break
    if num=='q':
        break
print('您购物车已经选好的商品为：')
for i in range(len(gift)-1,-1,-1):  #逆序输出
    print(gift[i])
'''

'''
dict_ticket={'G11':['北京南-天津南','19:02','20.01','59'],
             'G12':['杭州南-重庆北','19:02','21.02','1：59'],
             'G13':['杭州东-拉萨北','9:02','22.02','11：59']}
for item in dict_ticket:
    print(item,end='\t\t')
    for i in dict_ticket[item]:
        print(i,end='\t\t')
    print()

d={'a':['1','2'],
   'b':'2',
   'c':'3'}
for item in d:
    print(item,end='\t\t')
    for i in d[item]:
        print(i,end='\t\t')
    print()'''

'''
coffee_name=('蓝山','猫屎','拿铁','卡布奇诺','美式')
print('本店经营的咖啡有：')
for i,value in enumerate(coffee_name):
    print(i+1,'.',coffee_name[i],end='\t')
print()
choose=int(input('输入你想要点的咖啡编号：'))
if 0<choose<=len(coffee_name):
    print(f'你的{coffee_name[choose-1]}做好了')'''


#统计字符串中出现指定字符的次数
str="hellopython,Hellojava,hellodjango"
ipt=input('请输入你要统计的字符')
lst=[]
for item in range(len(str)):
    if ipt is str[item]:
        lst.append(item)
print(lst)
print(len(lst))

'''
#回文数
x=input('输入一个数')
y=x[::-1]
if x==y:
    print('true')
else:
    print('false')
'''








