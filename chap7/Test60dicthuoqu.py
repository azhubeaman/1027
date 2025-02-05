#作者：Ourjune
#开发时间：2021/11/16 7:41
#字典元素获取


#第一种方法
scores={'张三':100,'李四':98,'王五':45}
print(scores['张三'])
#print(scores['1211'])  #查找键不存在，会报错
#第二种方法
print(scores.get('张三'))
print(scores.get('1211'))#查找键不存在，不会报错 ：none
print(scores.get('陈六',99))#99是查找‘陈六’不存在时提供的默认值


