#作者：Ourjune
#开发时间：2021/11/19 8:04
#字符串大小写转换操作方法

s='hello,python'
print(s,id(s))
a=s.upper()
print(a,id(a))  #id不同，转成大写之后，会产生新的字符串对象
b=s.lower()
print(b,id(b))
print(b==s)
print(b is s)  #驻留机制

s2='hello,Python'
print(s2.swapcase())  #大写转成小写，小写转成大写
print(s2.capitalize())#第一个字符转换成大写，其余小写
s3='hello,python'
print(s3.title()) #每个英文单词的首字母变成大写，其余变成小写