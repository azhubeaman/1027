#作者：Ourjune
#开发时间：2021/12/8 7:39
#字符串的编码、解码转换

s='天涯共此时'
#编码
print(s.encode(encoding='GBK'))  #在GBK这种编码格式中，一个中文占两个字节
print(s.encode(encoding='UTF-8'))#在UTF-8这种编码格式中，一个中文占3个字节

#解码
#byte代表一个二进制数据（字节类型的数据）
byte=s.encode(encoding='GBK')#编码
print(byte.decode(encoding='GBK'))#解码
#print(byte.decode(encoding='UTF-8')) 报错，编码解码格式要统一

