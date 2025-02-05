#作者：Ourjune
#开发时间：2021/12/28 8:10
'''
1、abspath(path) 用于获取文件或目录的绝对路径
2、exists(path)  用于判断文件或目录是否存在，如果存在返回T，不存在返回F
3、join(path,name)将目录与目录或者文件名拼接起来
4、splitext() 分离文件名和扩展名
5、basename(path) 从一个目录中提取文件名
6、dirname(path) 从一个路径中提取文件路径，不包括文件名
7、isdir(path) 用于判断是否为路径
'''

import os.path

print(os.path.abspath('Test129_2.py'))
print(os.path.exists('F:\\PYfile\\1027\\chap14\\Test129_4.py'))
print(os.path.join(os.getcwd(),'Test1111.py'))

print(os.path.split('F:\\PYfile\\1027\\chap14\\Test129.py'))
print(os.path.splitext('Test123.py'))

print(os.path.basename('F:\\PYfile\\1027\\chap14\\Test129.py'))
print(os.path.dirname('F:\\PYfile\\1027\\chap14\\Test129.py'))
print(os.path.isdir('F:\\PYfile\\1027\\chap19\\'))#没有这个目录

print('---------------')
