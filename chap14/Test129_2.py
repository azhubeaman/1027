#encoding=UTF-8
#作者：Ourjune
#开发时间：2021/12/27 8:38
#文件对象常用方法
'''
6、seek(offset[,whence]) offset表示相对于whence的位置 whence默认为0，表示从文件头开始计算，1表示当前位置开始，2从文件尾开始计算
7、flush()
8、close()
'''

file=open('a.txt','r')
file.seek(2) #跳过两个字节；一个中文表示2个字节
print(file.read())
print(file.tell())  #指针所在的位置
file.close()