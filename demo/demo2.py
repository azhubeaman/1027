#作者：Ourjune
#开发时间：2022/1/10 19:49

nums=[2,7,11,15]
target=18
d = {}
for i in range(len(nums)):
    if target - nums[i] in d:
        print([i, d[target - nums[i]]])
    d[nums[i]] = i
'''
lst = [2, 5, 7, 11]
he = 9
d = {}  # {2:0,5:1,}
# 输出[0,2]或者[2,0]
for i, value in enumerate(lst):
    #print(i, value)
    if he - lst[i] in d:
        print([i, d[he - lst[i]]])
    d[lst[i]] = i
'''