#作者：Ourjune
#开发时间：2021/12/28 7:53

#练习
with open('copylogo.png','rb') as src_file:
    with open('copylogo2.png','wb') as target_file:
        target_file.write(src_file.read())