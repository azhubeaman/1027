#作者：Ourjune
#开发时间：2021/10/29 8:03
#对象的bool值

#每个对象都有布尔值
#验证对象的bool值
print('----------------以下对象bool都为False----------')
print(bool(False)) #False
print(bool(0))     #False
print(bool(0.0))   #False
print((bool(None)))#False
print(bool(''))    #空字符串
print(bool([]))    #空列表
print(bool(list()))#空列表
print(bool(()))    #空元组
print(bool(tuple()))#空元组
print(bool({}))    #空字典
print(bool(dict()))#空字典
print(bool(set())) #空集合
print('---------------其余对象bool值都为True----------')
print(bool(121.1))