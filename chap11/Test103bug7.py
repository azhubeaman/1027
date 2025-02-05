#作者：Ourjune
#开发时间：2021/12/21 8:37
#Traceback

#print(10/0)  #Traceback

import traceback
try:
    print('===========')
    print(1/0)
except:
    traceback.print_exc()    #有时候’=======‘会在前面，有时候会在后面，后续涉及


#此模块在后续log日志中会用到