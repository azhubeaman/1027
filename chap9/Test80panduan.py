#作者：Ourjune
#开发时间：2021/11/19 8:27
#字符串判断
'''
1、isidentifier()判断指定的字符串是不是合法的标识符
2、isspace()判断指定的字符串是否全部由空白字符组成（回车，换行，水平制表符）
3、isalpha()判断指定的字符串是否全部由字母组成
4、isdecimal()判断指定字符串是否全部由十进制的数字组成
5、isnumeric()判断指定的字符串是否全部由数字组成
6、isalnum()判断指定字符串是否全部由字母和数字组成
'''
#isidentifier()
print('1.','hello,Python'.isidentifier()) #判断是否是合法的字符串  #false，因为有，
print('2.','hello'.isidentifier()) #True
print('3.','张三_'.isidentifier())  #True
print('4.','张三-'.isidentifier()) #false
#isspace()
print('5.','\t'.isspace())
#isalpha()
print('6.','abc'.isalpha())
print('7.','张三'.isalpha())
print('8.','abc1'.isalpha())
#isdecimal()
print('9.','123'.isdecimal())
print('10.','123四'.isdecimal())
print('11.','ⅠⅡⅢⅣ'.isdecimal())
#isnumeric()
print('12.','123'.isnumeric())
print('13.','123四'.isnumeric()) #中文为TRUE
print('14.','ⅠⅡⅢⅣ'.isnumeric())#罗马数字TRUE
#isalnum()
print('15.','a123'.isalnum())
print('16.','a1_23'.isalnum())  #_不属于字母或数字
print('17.','张三321'.isalnum())