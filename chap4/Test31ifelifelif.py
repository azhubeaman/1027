#作者：Ourjune
#开发时间：2021/10/29 8:25
#多分支结构

#90-100 A
#80-89 B
#70-79 C
#60-69 D
#0-59 E
#小于0或者大于100 为非法数据（不是成绩有效范围）
num=int(input('请输入一个成绩：'))
if  num>=90 and num<=100:
    print('你的等级为A')
elif num>=80 and num<=89:
    print('你的等级为B')
elif num>=70 and num<=79:
    print('你的等级为C')
elif num>=60 and num<=69:
    print('你的等级为D')
elif num>=0 and num<=59:
    print('你的等级为E')
else:
    print('对不起，你的成绩不合法，不在有效范围内')

#优化：num>=90 and num<=100  可以写成90<=num<=100  只有python支持这样写
