#作者：Ourjune
#开发时间：2021/11/16 7:46

'''key的判断'''
scores={'张三':100,'李四':98,'王五':45}
print('张三'in scores)
print('张三'not in scores)

'''删除'''
print(scores)
del scores['张三'] #删除指定的键值对
print(scores)

#scores.clear() #清空字典元素
#print(scores)
'''新增元素'''
scores['陈六']=98 #新增元素
print(scores)
'''修改元素'''
scores['陈六']=91+2
print(scores)
