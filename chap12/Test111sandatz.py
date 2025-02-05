# 作者：Ourjune
# 开发时间：2021/12/22 8:31
# 面向对象的三大特征
# 封装：提高程序安全性
# 继承：提高代码的复用性
# 多态：提高程序的可扩展性和可维护性

class Car:
    def __init__(self,brand,price):
        self.brand = brand
        self.__price=price  #不允许被外部使用
    def start(self):
        print('汽车已启动')
    def buy(self):
        print(self.brand,self.__price)

car1=Car('奔驰','30w')
car1.buy()

print(car1.brand)
#print(car1.__price) 因为前面定义了不被外部使用，所以报错了
#print(dir(car1)) #中含有 _Car__price
print(car1._Car__price)  #在类的外部可以通过_Car__price进行访问  （不建议这样方式访问，因为定义的时候意思就是不允许访问，所以后续尽量也不要用到）