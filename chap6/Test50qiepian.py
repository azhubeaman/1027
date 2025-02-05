#作者：Ourjune
#开发时间：2021/11/3 7:51
#获取多个列表元素，切片操作

lst=[10,20,30,40,50,60,70,80]
print(lst[1:6:1])  #start=1,stop=6,step=1
print('原列表id：',id(lst))
lst2=lst[1:6:1]
print('切完之后id：',id(lst2))  #id不同

#step默认步长为1
print(lst[1:6])
#省略step
print(lst[1:6:])
#省略start
print(lst[:6:2])
#省略stop
print(lst[1::2])#会输出到最后一个元素
print('------------------step为负数--------------')
print('原列表：',lst)
print(lst[::-1])
#start=7,stop省略，step=-1
print(lst[7::-1])

print(lst[6:0:-2])