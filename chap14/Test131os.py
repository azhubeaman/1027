#作者：Ourjune
#开发时间：2021/12/28 7:59
import os
#os.system('notepad.exe')
#os.system('calc.exe')

#调用可执行文件
#os.startfile('E:\\foxmail\\Foxmail.exe')

print(os.getcwd())
lst=os.listdir('../chap14')
print(lst)

#os.mkdir('newdir')#创建目录
os.makedirs('newdir/sub')#创建多级目录
#os.rmdir('newdir')#移除目录
#os.removedirs('A/B/C')#移除多级目录

os.chdir('F:\\PYfile\\1027\\chap13')#设置当前目录
print(os.getcwd())
