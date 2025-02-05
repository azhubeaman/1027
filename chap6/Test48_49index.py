#作者：Ourjune
#开发时间：2021/11/3 7:43
#获取指定元素的索引

lst=['hello','world',98,'hello']
print(lst.index('hello'))#0   如果列表里有相同元素，只返回列表中相同元素的第一个元素的索引
#print(lst.index('p'))  #valueError:'p' is not in list
#print(lst.index('hello',1,3))#valueError:'hello' is not in list

#获取列表中指定的元素
lst2=['hello','world',98,'hello','world',123]
#获取索引为2的元素
print(lst2[2])
#获取索引为-3的元素
print(lst2[-3])
#获取索引为10的元素
#print(lst2[10])   IndexError: list index out of range