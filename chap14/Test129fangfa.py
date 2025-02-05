#encoding=UTF-8
#作者：Ourjune
#开发时间：2021/12/27 8:38
#文件对象常用方法
'''
1、read[size]
2、readline()
3、readlines()
'''

file=open('b.txt','r')
#print(file.read())
#print(file.readline())
print(file.readlines())
file.close()