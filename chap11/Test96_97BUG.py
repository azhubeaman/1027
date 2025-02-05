#作者：Ourjune
#开发时间：2021/12/13 16:07
'''
常见语法错误：
1、漏了末尾的冒号，如if语句，循环语句，else子句等
2、缩进错误
3、把英文符号写成中文符号，比如说：引号，冒号，括号
4、字符串拼接的时候，把字符串和数字拼在一起
5、没有定义变量，比如说while的循环条件的变量
6、== 比较运算符和= 赋值运算符的混用
'''
#语法错误（
#age=input('请输入你的年龄')
#if age<=18:  不加int，类型转换错误
#    print('你未成年')

#i没有定义，且死循环了
'''
    while i < 10:
        print(i)
'''
#SyntaxError
for i in range(3):
    username=input('账户：')
    passwd=input('密码：')
    if username=='zml' and passwd=='123':
        print('登录成功')
        break
    else:
        print('请再次输入')
print('输入三次失败，程序退出')