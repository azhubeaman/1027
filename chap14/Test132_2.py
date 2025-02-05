#作者：Ourjune
#开发时间：2021/12/28 8:28

#练习：列出指定目录下的所有py文件
import os.path
paaath=input('请输入一个地址：')
if os.path.exists(paaath):  #判断地址是否存在
    lst=os.listdir(paaath)  #获取当前目录下所有文件，放进列表
    for filename in lst:    #遍历列表
        if filename.endswith('.py'): #判断后缀是否是py文件
            print(filename) #输出该目录下的py文件
else:
    print('输入的地址不存在')