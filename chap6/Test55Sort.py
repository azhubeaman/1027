#作者：Ourjune
#开发时间：2021/11/8 8:26
#列表排序

lst=[10,20,30,40,25,34]
lst.sort()
print(lst) #id没有发生更改

#通过指定关键字参数，进行降序
lst.sort(reverse=True)   #True是降序，False是升序
print(lst)

#调用内置函数sorted(),将产生新的列表对象
print('---------------')
lst1=[10,20,30,40,25,34]
print('原列表',lst1)
new_list1=sorted(lst1)
print(lst1)
print(new_list1)  #id会变，因为产生了一个新的列表对象

