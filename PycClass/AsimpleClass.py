# 定义一个空类
class NullClass:
    pass

# 定义一个具有意义的类
class Animal:
    # 类的属性
    count = 0
    legs = []
    # 类的初始化函数（等级于java构造函数）
    def __init__(self,name):
        self.name = name

    # 类的方法
    def eat(self):
        print("i can eat")

# 类中必须要有初始化函数， 初始化函数在对象创建时自动调用，用于初始化对象中数据

# 任何Python 类方法的第一个参数都是self, 该关键字等价于java中 this,self 指向新创建对象。

if __name__ == '__main__':
    # 类的实例化，创建对象
    dog = Animal('dog')
    dog.eat()
