#作者：Ourjune
#开发时间：2021/11/17 7:49
#集合间的关系

'''两个集合是否相等（元素相同，就相等）'''
s1={1,2,34,41}
s2={2,1,41,34}
print(s1==s2)
print(s1!=s2)

'''一个集合是否是另一个集合的子集'''
s3={1,2,34,41,55,44}
s4={1,2,34,41}
s5={1,2,34,90}
print(s4.issubset(s3)) #表示s4是s3的子集吗
print(s5.issubset(s3))

'''一个集合是否是另一个集合的超集'''
print(s3.issuperset(s4)) #表示s3是s4的超集吗（s3是否包含了s4）

'''两个集合是否含有交集'''
print(s4.isdisjoint(s5)) #false 有交集为false
s6={11,22,324}
print(s5.isdisjoint(s6)) #True  无交集为true
