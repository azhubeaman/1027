#作者：Ourjune
#开发时间：2021/11/3 8:03
#列表元素的判断与遍历

#判断
lst=[10,20,'python','hello']
print(10 in lst) #true
print(100 in lst)#false
print(10 not in lst)#false

#遍历
for item in lst:
    print(item,end='\t')