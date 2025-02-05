#作者：Ourjune
#开发时间：2021/3/12 7:10
#字符串的切片操作
#字符串是不可变类型：不具备增删改，切片操作将产生新的对象
s='hello,Python'
print(s[0:4])
print(s[6:])
s1=s[:5]+'!'+s[6:]
print(s1)
#完整写法
print('---------[start:end:step]-----------')
print(s[1:5])
print(s[4:0:-1])
print(s[::2])
print(s[::-1])



