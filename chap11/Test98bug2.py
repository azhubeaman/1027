#作者：Ourjune
#开发时间：2021/12/21 7:36
#知识点不熟练引起的错误


#索引越界问题
lst=[11,22,33,44]
#print(lst[4])  #IndexError: list index out of range
print(lst[3])

lst2=[]
#lst=append('A','B','C')  #append方法是lst的，所以前面要加上lst.  且append每次只能加一个元素
lst2.append('A')
lst2.append('B')
print(lst2)