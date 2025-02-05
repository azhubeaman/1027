#作者：Ourjune
#开发时间：2021/11/19 8:45
#字符串的替换与合并

'''
1、字符串的替换：replace()，第一个参数指定被替换的子串
2、字符串的合并：join()，将列表或元组中的字符串合并成一个字符串
'''

s='hello,Python'
print(s.replace('Python','java'))
s1='hello,Python,Python,Python'
print(s1.replace('Python','java',2)) #替换两次

#join
lst=['hello','Java','Python']
print('|'.join(lst))
print(''.join(lst))

t=('hello','Java','Python')
print(''.join(t))

print('*'.join('Python'))