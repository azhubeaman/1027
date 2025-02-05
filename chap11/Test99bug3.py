#作者：Ourjune
#开发时间：2021/12/21 7:41
#思路不清导致的问题
'''
使用print函数拍查
使用#暂时注释掉部分代码
'''
#题目要求：豆瓣T250排行，使用列表存储电影信息，要求输入名字在屏幕上显示XXX出演了哪部电影
lst=[{'rat':[9.2],'id':'123','type':['剧情','犯罪'],'title':'肖生客的救赎','actors':['罗宾斯','摩根']},
     {'rat':[9.1],'id':'234','type':['剧情','爱情','同性'],'title':'霸王别姬','actors':['张国荣','葛优']},
     {'rat':[9.4],'id':'345','type':['剧情'],'title':'阿甘正传','actors':['汤姆·汉克斯','罗宾·怀特']}
     ]
name=input('请输入你要查找的演员：')
for item in lst:
    actors=item['actors']
    for actor in actors:
        if name in actor:
            print(name,'出演了',item['title'])