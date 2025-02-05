#作者：Ourjune
#开发时间：2021/12/28 7:45


#with不需要手动写close方法释放资源
print(type(open('a.txt','r')))
with open('a.txt','r') as file:  #open('a.txt','r')为上下文管理器
    print(file.read())

