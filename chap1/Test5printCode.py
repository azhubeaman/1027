#作者：Ourjune
#开发时间：2021/10/27 7:32
#print用法

#可以输出数字
print(1111)

#可以输出字符串
XXX='1'
print(XXX)
print(XXX,type(XXX))
print("helloworld")
print('helloworld')

#含有运算符的表达式
print(1+3)

#输出到文件中
#注意点：1、所指定的盘符存在 2、使用file=fp
fp=open('F:/test.txt','a+') #a+的意思是读写的方式打开文件，如果没有就创建，没有就在文件的后面（后一行）追加
print("helloworld2",file=fp)
fp.close()

#不进行换行输出（输出内容在一行中）
print(1,2,3,4)