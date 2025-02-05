#作者：Ourjune
#开发时间：2021/11/3 8:07
#列表元素的增删改

#append()
lst=[10,20,30]
print('添加之前:',lst,'id:',id(lst))
lst.append(100)
print('添加之后',lst,'id:',id(lst))

#extend
lst2=['hello','world']
#lst.append(lst2)
#print(lst) #将lst2作为一个元素添加到列表末尾
lst.extend(lst2)
print(lst,id(lst))

#insert
#在任意位置上添加一个元素
lst.insert(1,333) #索引为1的位置上加333
print(lst)

#切片
#在列表的任意位置添加至少一个元素
lst3=[True,False,'hello']
lst[1:]=lst3  #1的意思是指从索引为1开始的切掉，替换为lst3中的内容
print(lst)