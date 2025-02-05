#作者：Ourjune
#开发时间：2021/11/17 7:42
#集合的相关操作

s={1,2,34,41,22,122}
print(1 in s) #判断
s.add(101)
print(s)
s.update({100,200,400}) #
print(s)
s.update([201,202,203])
s.update((301,302,312))
print(s)

'''集合元素的删除'''
s.remove(100)
print(s)
#s.remove(500)  #KeyError: 500
#print(s)
s.discard(500) #这种删除方式不会抛异常
print(s)
print('------------')
s.pop()
print(s)
s.pop()
print(s)
#s.pop(400)  #TypeError: pop() takes no arguments (1 given)
#print(s)  pop()不能指定入参删除

#s.clear() #清空集合元素
print(s)