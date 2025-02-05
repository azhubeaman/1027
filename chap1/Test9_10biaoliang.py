#作者：Ourjune
#开发时间：2021/10/27 8:31
#变量的定义和使用
name="玛丽亚"
print(name)
#变量由三部分组成
#1、标识：表示对象所存储的内存地址，使用内置函数id(obj)来获取
#2、类型：表示的是对象的数据类型，使用内置函数type(obj)来获取
#3、值：表示对象所存储的具体数据，使用print(obj)具体输出
#内存中存储的是id
print('标识',id(name))
print('类型',type(name))
print('值',name)
#变量多次赋值后，指向新的空间
name='阿凡达'
print(name)
