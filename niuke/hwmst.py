#作者：Ourjune
#开发时间：2022/2/24 20:38
'''
#输入一个字符串，不满8位，其余补0；满8位换行补0
def prtstring(string):
    if len(string)<8:
        print(string+"0"*(8-len(string)))
    else:
        print(string[0:8])
        print(string[8:]+"0"*(8-len(string[8:])))
a=input()
b=input()
prtstring(a)
prtstring(b)
'''
'''
#获取字符串最后一个单词的长度
def prtstring(a):
    lst=a.split()
    strlast=lst[-1]
    print(len(strlast))
a=input()
prtstring(a)
'''
'''
#统计字符在字符串中出现的个数
a=input().upper()
b=input().upper()
n=0
for i in a:
    if b==i:
        n=n+1
print(n)
'''
'''
while True:
    try:
        string=input()
        if len(string)<8:
            print(string+"0"*(8-len(string)))
        else:
            print(string[0:8])
            string=string[8:]+'0'*(8-len(string[8:]))
            print(string)
    except:
        break
        '''

'''
#连续输入字符串，请按长度为8拆分每个输入字符串并进行输出；
#长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
while True:
    try:
        string = input()
        i = len(string) // 8
        if len(string)%8==0:
            for item in range(i):
                a = string[8 * item:8 * (item + 1)] + '0' * (8 - len(string[8 * item:8 * (item + 1)]))
                print(a)
        else:
            for item in range(i + 1):
                a = string[8 * item:8 * (item + 1)] + '0' * (8 - len(string[8 * item:8 * (item + 1)]))
                print(a)
    except:
        break
'''
'''
#讲一个十六进制的数转换成十进制
#方法一：print(int(input(),16))
#方法二：
while True:
    try:
        a=input()
        numbs=a.split('0x')[1]
        numbs_lst=list(numbs)
        numbs_lst.reverse()
        m=0
        for i in range(len(numbs_lst)):
            b=numbs_lst[i]
            if b=='A':
                b=10
            elif b=='B':
                b=11
            elif b=='C':
                b=12
            elif b=='D':
                b=13
            elif b=='E':
                b=14
            elif b=='F':
                b=15
            m=m+(16**i)*int(b)
        print(m)
    except:
        break
'''
'''
#输入一个数，输出它的质数因子，用空格分开
num=180
for item in range(2,num):
    while num%item==0:
        print(item,end=' ')
        num=num//item
    for j in range(2,num):
        if num%j==0:
            num = num // j
            print(j,end=' ')
            break
    else:
        if num!=1:
            print(num,end=' ')
            break
'''
'''
#合并表记录，运用动态字典解！
a=int(input())
d={}
for i in range(a):
    b=input().split()
    print(b,type(b))
    key=int(b[0])
    print(key,type(key))
    value=int(b[1])
    d[key]=d.get(key,0)+value
for j in sorted(d):
    print(j,d[j])
'''
'''
#统计ascll码值在0到127之间的字符个数，去重
count=0
a='aaaa-b'
a=''.join(set(a))
print(a)
for i in a:
    if 0<=ord(i)<=127:
        count+=1
print(count)
'''
'''
#输出最长连续子字符串的个数
a='aabweq'
b='gggg'  #3 2+1,4 3+2+1,5 4+3+2+1
c=[]
if len(a)<len(b):
    a,b=b,a
for j in range(1,len(b)+1):
    for i in range(j):
        if b[i:j] in a:
            c.append(len(b[i:j]))
        else:
            c.append(0)
c.sort()
print(c[-1])
'''
'''
#质数因子
num=int(input())
if num!=1:
    for i in range(2,num):
         while num%i==0:
                print(i,end=' ')
                num=num//i
'''

#38题
'''给定一个url前缀和url后缀
        通过,分割 需要将其连接为一个完整的url
        如果前缀结尾和后缀开头都没有/
        需要自动补上/连接符
        如果前缀结尾和后缀开头都为/
        需要自动去重
        约束：
         不用考虑前后缀URL不合法情况

         输入描述
         url前缀(一个长度小于100的字符串)
         url后缀(一个长度小于100的字符串)
         输出描述
         拼接后的url'''
'''一、输入/acm,/bb 输出/acm/bb
   二、输入/abc/,/bcd 输出/abc/bcd
   三、输入/acd,bef输出/acd/bef
   四、输入,输出/
'''
'''
a=input()
if a!=',':
    a=a.split(',')
    if a[0][-1]!= '/':
        a[0]=a[0]+'/'
    if a[1][0] is '/':
        a[1]=a[1][1:]
    print(a[0] + a[1])
else:
    print('/')
'''

'''
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
例如，当输入5时，应该输出的三角形为：
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11
'''
'''
a=int(input())
start=1
for i in range(0,a):
    start=start+i
    c=start
    print(c,end=' ')
    for j in range(1,a-i):
        c=c+j+i+1
        print(c,end=' ')
    print()
'''

a=[2, 2, 4, 5]
b={0}
for i in a:
    for j in list(b):
        b.add(i+j)
print(b)
