#作者：Ourjune
#开发时间：2021/10/29 8:40
#嵌套if

'''会员 >=200  8折
       >=100  9折
       不打折
    非会员 >=200  9.5折
        不打折'''
answer=input('您是会员吗？y/n')
price = float(input('请输入你的购物金额：'))
if answer=='y':  #会员
    if price>=200:
        print('打8折，您的付款金额为：',price*0.8)
    elif price>=100:
        print('打9折，您的付款金额为：',price*0.9)
    else:
        print('不打折，您的付款金额为：',price)
else:   #非会员
    if price>=200:
        print('打9折，您的付款金额为：',price*0.9)
    else:
        print('不打折，您的付款金额为',price)


