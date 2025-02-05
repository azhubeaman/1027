#作者：Ourjune
#开发时间：2021/12/27 8:31

src_file=open('logo.png','rb')
target_file=open('copylogo.png','wb')
target_file.write(src_file.read())  #边读边写
target_file.close()