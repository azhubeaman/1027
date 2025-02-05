#作者：Ourjune
#开发时间：2021/11/16 8:34
'''元组的遍历'''

t=('Python','world',98)
for item in t:
    print(item)


#也可以用索引的方式，但是得知道元组内有多少元素
print(t[2])
#print(t[3])  #IndexError: tuple index out of range