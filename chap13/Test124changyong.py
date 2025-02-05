#作者：Ourjune
#开发时间：2021/12/24 8:34

#常用模块
import sys  #py解释器及其环境操作相关的标准库exec_prefix = 'C:\\BuildAgent\\system\\.persistent_cache\\pythons\\python36' 解释器的安装位置
print(sys.getsizeof(24)) #获取对象所占内存大小
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

import time  #提供时间相关的各种函数的标准库
print(time.time())
print(time.localtime(time.time()))
print('------------------------------------')

import urllib.request #urllib是一个包  用于读取来自网上的数据标准库
print(urllib.request.urlopen('http://www.baidu.com').read())

