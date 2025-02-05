#作者：Ourjune
#开发时间：2021/12/22 19:24
#多态
#java是静态语言，python是动态语言（鸭子类型）
class Animal():
    def eat(self):
        print('动物会吃..')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Person():
    def eat(self):
        print('人吃五谷杂粮')
#定义一个函数调用eat方法
def fun(obj):
    obj.eat()

fun(Cat())
fun(Dog())
fun(Animal())
fun(Person())   #特殊，动态绑定方法