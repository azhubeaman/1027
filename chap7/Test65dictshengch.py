#作者：Ourjune
#开发时间：2021/11/16 8:02
#最后有知识点总结

#字典生成式
#内置函数zip()  用于将可迭代的对象最为参数

items=['Fruits','Books','Others']
print(type(items))
prices=[91,23,32,1]
d={items:prices for items,prices in zip(items,prices)}
print(d)  #以元素少的为基准打包匹配的
d={items.upper():prices for items,prices in zip(items,prices)}#upper()转大写
print(d)