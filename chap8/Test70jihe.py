#作者：Ourjune
#开发时间：2021/11/16 8:37
#什么是集合
#与列表，字典一样都属于可变类型的序列
#集合是没有value

#使用{}创建
s={'Python','hello',5,5,6,6}   #不允许重复，会去重
print(s)

#使用set()创建
s1=set(range(6))
print(s1,type(s1))

s2=set([1,2,3,34,4,5,5,1]) #将列表转换成集合
print(s2)

s3=set((1,2,3,3,4,5,64))  #64跑到前面去了，说明集合是无序的
print(s3)

s4=set('PYthon')
print(s4)

s5=set({123,12,3,24,22,12,21})
print(s5)
print('==========')
#定义一个空集合,不能用s6={}，这样是空字典
s6=set()
print(s6,type(s6))
