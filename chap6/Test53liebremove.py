#作者：Ourjune
#开发时间：2021/11/3 8:28

#remove
lst=[10,20,10,20,30,40,50]
lst.remove(10)
print(lst)  #只会移除重复元素的第一个元素

#pop
#按索引删除
lst.pop(1)
print(lst)  #移除索引为1的元素
#lst.pop(100) #IndexError: pop index out of range,索引位置不存在，报错
lst.pop()
print(lst) #不指定索引位置，默认删除最后一个

#切片
#删除至少一个元素，将产生新的列表对象
new_list=lst[1:3]
print('原列表',lst,id(lst))
print('切片后',new_list,id(new_list))

'''不产生新的列表对象，而是删除源列表中的内容'''
lst[1:3]=[]
print(lst)

'''清除列表中的所有元素'''
lst.clear()
print(lst)

'''将列表删除'''
lst2=[1,2,3]
del lst2
#print(lst2)不存在的对象，报错