#作者：Ourjune
#开发时间：2021/11/16 7:55
#字典元素的遍历

scores={'张三':100,'李四':98,'王五':45}
for i in scores:
    print(i,scores[i],scores.get(i))  #两种遍历方式

d={'name':'张三','name':'李四'}
print(d)  #李四把张三覆盖，因为key不允许重复
d1={'name':'张三','name2':'张三'}
print(d1) #value可以重复

