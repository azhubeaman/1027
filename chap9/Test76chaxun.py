#作者：Ourjune
#开发时间：2021/11/17 8:41
#字符串查询

s='hello,hello'
print(s.index('h'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))

#print(s.index('k'))  ValueError: substring not found
print(s.find('k'))#返回-1    这就是find和index唯一的差异

