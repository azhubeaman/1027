#作者：Ourjune
#开发时间：2021/11/23 8:02
#字符串的比较操作
#比较的是字符的原始值 ord chr

print('apple'>'app') #True
print('apple'>'banana')#False
print(ord('a'),ord('b'))
print(chr(97),chr(98))
print(ord('朱')) #26417
print(chr(26417))

a=b='Python'
c='Python'
print(a==b)
print(b==c)
print(a is b)
print(a is c)