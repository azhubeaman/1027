#作者：Ourjune
#开发时间：2021/11/19 8:13
#字符串内容对齐
s='hello,Python'

#居中对齐
print(s.center(20,'*'))  #20代表20个字符

#左对齐
print(s.ljust(20,'*'))
print(s.ljust(10))  #小于实际长度，返回原字符
print(s.ljust(20)) #没有填充符，默认为空格

#右对齐
print(s.rjust(20,'*'))
print(s.rjust(20))

#右对齐，使用0进行填充
print(s.zfill(20))
print(s.zfill(10))
#特殊：
print('-8910'.zfill(8))  #加上- 一共是8位
print('----------------------------')

print('♥'.center(20))
for i in range(3,20,2):
    print((i*'*').center(20))
print('|   |'.center(20))