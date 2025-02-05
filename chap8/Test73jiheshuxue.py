#作者：Ourjune
#开发时间：2021/11/17 7:57
#集合的数学操作

#交集
s1={10,20,30,40}
s2={20,30,40,50,60}
print(s1.intersection(s2))
print(s1 & s2)  #& 与 intersection()等价

#并集
print(s1.union(s2))
print(s1 | s2) #union与|等价

'''交集和并集之后原集合都没有发生变化'''

#差集操作
print(s1.difference(s2)) #s1集合减去s2集合，剩余10
print(s1-s2)

#对称差集
print(s1.symmetric_difference(s2)) #去掉相同的，剩余的组成集合
print(s1^ s2)