#作者：Ourjune
#开发时间：2021/10/29 7:30
#bool运算符

a,b=1,2
print('----------and 并且--------------')
print(a==1 and b==2) #True and True 结果为true
print(a==1 and b<2)  #True and False 结果为False
print(a!=1 and b==2) #False and True 结果为False
print(a!=1 and b!=2) #False and False 结果为False

print('------------or 或者-------------')
print(a==1 or b==2) #True or True 结果为True
print(a==1 or b<2)  #True or False 结果为True
print(a!=1 or b==2) #False or True 结果为True
print(a!=1 or b!=2) #False or False 结果为False

print('----------------not 对bool类型的操作数进行取反 -------------')
f=True
f2=False
print(not f)
print(not f2)

print('-------------in与not in------------')
s='helloworld'
print('w' in s)
print('k' in s)
print('w'not in s)
