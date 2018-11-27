#!/usr/bin/python3
# --coding=UTF-8--

def dictionaryTest():
    # 字典创建
    dict1 = {}
    dict2 = dict([('name','jack'),('sex','male')])
    print("dict1=",dict1,",dict2=",dict2)

    # 字典访问
    name = dict2['name']
    print('name is: %s'%name)

    # 赋值
    dict2['age'] = '24'
    print("dict2 = ",dict2)

    # 直接修改value
    dict2['sex'] = 'female'
    print("dict2 = ",dict2)

    # get() 方法获取值
    age = dict2.get('age')
    print("age = %s"%age)

    # update() 方法更新 dict
    dict2.update([('dept','cloud'),('position','engineer')])    
    print("dict2 = ",dict2)

    # items()方法， 以列表返回可遍历的元组数组 
    rst1 = dict2.items()
    print('rst1=',rst1)

    # keys()方法， 以列表形式返回所有键
    rst2 = dict2.keys()
    print("rst2 = ",rst2)

    # values()方法， 以列表形式返回所有值
    rst3 = dict2.values()
    print("rst3 = ",rst3)

    # pop() 方法 ，删除并返回被删除的键值对
    key_val = dict2.pop("sex")
    print("key_val = %s"%key_val)

    # popitem() 方法， 随机删除并以元组形式返回一个键值对
    key_val2 = dict2.popitem()
    print("key_val2 =",key_val2)

    # clear() 清楚字典
    dict2.clear()
    print("dict2 = ",dict2)

if __name__ == "__main__":
    dictionaryTest()