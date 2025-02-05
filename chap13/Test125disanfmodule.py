#作者：Ourjune
#开发时间：2021/12/24 8:49

#第三方模块安装，用dos命令
#pip install 模块名
import  schedule
import time


def job():
    print('哈哈------')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)