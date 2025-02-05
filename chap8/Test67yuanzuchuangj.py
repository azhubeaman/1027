#作者：Ourjune
#开发时间：2021/11/16 8:17

'''第一种创建方式，使用（）'''
t=('Python','world',98)
print(t)
print(type(t))

#可以写成;
t2='Python','world',98
print(type(t2)) #（）可以省略

'''使用tuple()'''
t1=tuple(('Python','world',98))
print(t1)
print(type(t1))

'''只包含一个元组的元素需要使用逗号和小括号'''
t3=('Python')
t4=('Python',)
print(t3,t4)
print(type(t3),type(t4))

'''空元组的创建方式'''

#复习:空列表\空字典
lst=[]
lst1=list()

d=dict()
d1={}

t4=()
t5=tuple()
print('空列表：',lst,lst1)
print('空字典：',d,d1)
print('空元组：',t4,t5)