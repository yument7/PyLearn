#!/usr/bin/python3
# --coding=UTF-8--

def setTest():
    set1 = {'jack','cloudDept','Engineer'}
    set2 = set() # 定义空集合 ，不能用 {} 定义空集合，{} 表示空字典
    set3 = set('python_java')
    set4 = set('javascript')
    print('set1=',set1,' ,set2=',set2,' ,set3=',set3)

    # add() 方法，添加元素
    set1.add('5')
    print("add_set1=",set1)

    # update() 方法， 修改或添加元素, 参数为任意序列
    set1.update({'male','sz'})
    set1.update(('han','no'))
    print("update_set1=",set1)

    # remove() 方法， 删除元素
    set1.remove('sz')
    print("remove_set1=",set1)

    # & 运算 取交集
    set_x = set3 & set4
    print("set_x=",set_x)
    # | 运算 取并集
    set_x = set3 | set4
    print("set_x=",set_x)
    #  ^ 运算 取补集
    set_x = set3 ^ set4 
    print("set_x=",set_x)
    # - 运算
    set_x = set3 - set4
    print("set_x=",set_x)
    # == 运算
    set_x = set3 == set4
    print("set_x=",set_x)

if __name__ == "__main__":
    setTest()