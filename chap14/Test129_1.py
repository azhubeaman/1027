#作者：Ourjune
#开发时间：2021/12/27 8:41
'''
4、write(str)
5、writelines(s_list)

'''

file=open('a.txt','a')
#file.write('ppp')
lst=['java','go','python']
file.writelines(lst)
file.close()