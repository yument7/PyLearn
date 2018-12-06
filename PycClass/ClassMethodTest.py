class Device:
    valid = 1   # 公有类属性
    __rank = 1  # 私有类属性

    def __init__(self,deviceId,partNo,name,country,desc):
        self.__id = deviceId           # 私有实例属性 
        self.partNo = partNo     # 公有实例属性
        self.name = name
        self.country = country
        self.desc = desc
    
    # getter setter 方法
    def getId(self):
        return self.__id
    def setId(self,deviceId):
        self.__id = deviceId

    # 实例方法
    def toString(self):
        
        result = ''
        result = result + '_id:'+str(self.__id)+', partNo:'+self.partNo+', name:'+self.name\
        +', country:'+self.country+', desc:'+self.desc\
        +', valid:'+str(self.valid)+',__rank:'+str(self.__rank)
        print('result='+result)
        return result
    
    # 类方法 将类本身作为操作对象的方法, 参数使用类参数cls，可以调用类属性
    @classmethod 
    def printClassInfo(cls):
        print('rank=', cls.__rank)
        print(cls.__class__)
        print(dir(cls))
    # cls 就好比一个指向当前类的类对象，不能直接通过cls访问实例属性

    # 静态方法 静态方法没有参数限制，即不要实例参数self，也不需要类参数cls
    @staticmethod
    def getClassAttribute():
        print(Device.valid)
        print(Device.__rank)
    # 不能调用自身实例方法，不能访问实例属性

    # 私有方法
    def __getRank(self):
        return self.__rank

# 使用 __new__函数 实现单例模式
class Singleton:
    __instance = None
    def __init__(self):
        pass
    # 在 __init__之前调用
    def __new__(cls,*args,**kwargs):
        if  Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls,*args,**kwargs)
        return Singleton.__instance


if __name__ == '__main__':
    resistor = Device(259746,'p00001','片膜电阻器','china','number one resistor')
    resistor.toString()
    #resistor.printClassInfo()
    resistor.getClassAttribute()

    s1 = Singleton()
    s2 = Singleton()
    print(s1==s2)
