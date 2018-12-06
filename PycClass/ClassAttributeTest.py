class Device:
    valid = 1   # 公有类属性
    __rank = 1  # 私有类属性

    def __init__(self,deviceId,partNo,name,country,desc):
        self.__id = deviceId           # 私有实例属性 
        self.partNo = partNo     # 公有实例属性
        self.name = name
        self.country = country
        self.desc = desc
    
    def getId(self):
        return self.__id
    
    def setId(self,deviceId):
        self.__id = deviceId

if __name__ == '__main__':
    resistor = Device(259746,'p00001','片膜电阻器','china','number one resistor')
    
    # 类与实例访问 公有 类属性
    print('valid_c=', Device.valid)
    print('valid_o=', resistor.valid)
    # 类与实例访问 私有 类属性 无法进行访问
    # print('rank_c=', Device.__rank)   # 报错
    # print('rank_o=', resistor.__rank) # 报错

    # 类与实例访问 私有 实例属性 无法进行访问
    # print('id_c=', resistor.__id)
    # print('id_o=', resistor.__id)

    # 通过get set 方法 访问，修改私有属性
    print('id_cg=', resistor.getId())
    resistor.setId(335976)
    print('id_cs=', resistor.getId())

    # 通过实例访问 公有 实例属性
    print('name=',resistor.name,',country=',resistor.country)

    # 属性的修改
    Device.valid = Device.valid + 1
    print('valid_cu=', Device.valid)
    Device.valid = resistor.valid + 1
    resistor.valid = resistor.valid + 1
    print('valid_ouo=', resistor.valid)
    resistor.valid = Device.valid + 1
    print('valid_ouc=', Device.valid)
    print('valid_ouo=', resistor.valid)

    # 特殊属性
    print('name:', Device.__name__)
    print('doc:', Device.__doc__)
    print('bases:', Device.__base__)
    print('dict:', Device.__dict__)
    print('module:', Device.__module__)
    print('class:', Device.__class__)