#作者：Ourjune
#开发时间：2021/10/27 7:50
#转义字符
print('hello \nworld')  #\n表示newline表示换行

print('hello\tworld')
print('helloooo\tworld') #\t表示tab键，光标移动到下一组4个空格的开始处，占4个字符

print('hello\rworld') #r表示return，光标移动到本行开头，world将hello覆盖了

print('hello\bworld') #\b表示backspace,是退一个格，将o退没了

print('http:\\\\www.baidu.com')
print('老师说：\"大家好\"')
#原字符，不希望字符串中的转义字符起作用，就是使用原字符，在字符串之前加上R或者r
print(r'hello\nworld')
#注意点,最后一个字符不能是反斜杠
#print(r'hello\tworld\')
print(r'hello\tworld\\')#两个\\可以