#作者：Ourjune
#开发时间：2021/12/28 8:44

#遍历所有当前目录下所有目录下的py文件
import  os
pathh=os.getcwd()
#print(pathh)
files=os.walk(pathh)  #遍历该路径下所有文件目录
for dirpathhh,dirname,filename in files:
    '''print(dirpathhh)
    print(dirname)
    print(filename)
    print('=======')'''
    for dir in dirname:   #遍历所有文件夹
        pass
    for file in filename: #遍历所有文件
        if file.endswith('.py'):
            print(os.path.join(dirpathhh,file))


