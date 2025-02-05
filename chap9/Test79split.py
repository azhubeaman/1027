#作者：Ourjune
#开发时间：2021/11/19 8:19
#字符串分割

s='hello world                 |!  Python'
lst=s.split()  #不指定，默认用空格分割
print(lst)
#使用sep劈分
s1='hell0|world||Python'
print(s1.split(sep='|'))
print(s1.split('|'))
#使用maxsplit指定最大分几段
print(s1.split(sep='|',maxsplit=2))

print('----------------')
'''rsplit()从右侧开始劈分'''
print(s1.rsplit('|'))
print(s1.rsplit(sep='|',maxsplit=1))