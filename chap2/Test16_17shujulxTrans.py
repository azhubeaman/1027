#作者：Ourjune
#开发时间：2021/10/28 7:44
name='张三'
age=20
print(type(name),type(age))#说明name与age的数据类型不同
#print('我叫'+name+'今年'+age+'岁')#报错，解决方案，类型转换
print('我叫'+name+'今年'+str(age)+'岁')#通过str函数将其他数据类型转为字符串

print('-------str()将其他类型转成str类型---------')#也可以用引号转换
a=10
b=109.9
c=False
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))
#也可以用引号转换
print(type('a'),type('b'),type('c'))

print('----------int()将其他类型转换为int类型')
s1='122'
f1=98.22
s2='122,11'
ff=True
s3='hello'
print(int(s1),type(int(s1))) #将str转成int类型，前提是字符串为数字串
print(int(f1),type(f1))      #float转成int类型，截取整数部分
#print(int(s2),type(int(s2)))#报错，字符串为小数串
print(int(ff),type(int(ff))) #bool转int
#print(int(s3),type(int(s3)))#报错，字符串不为数字串

print('-----------float()函数，将其他数据类型转成float类型')
s1='122.99'
s2='76'
ff=True
s3='hello'
i=98
print(type(s1),type(s2),type(ff),type(s3))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(ff),type(float(ff)))
#print(float(s3),type(float(s3)))#报错，字符串中的数据如果是非数字串，则不允许转换
print(float(i),type(float(i)))