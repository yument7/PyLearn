#!/usr/bin/python3
# --coding=UTF-8--

def listTest():
    list1 = [1,2,3,4,5]
    list2 = list('abcd')
    list3 = list(('pear','peach','orange','apple'))
    list2[2] = "e" #修改元素值
    del list2[3]   # 删除元素
    print("list1=",list1,",list2[2]=",list2[2],",list3[1:3]=",list3[1:3])
    
    # append() 方法
    list3.append("banner")
    list3.append(["Litchi","potato"])       
    print("apend = ",list3)
    
    # ount() 方法
    number = list3.count('pear')
    print("count number = %d"%number)

    # extend() 方法
    list3.extend(('Tomatoes','ginger'))
    print("extend = ",list3)
    
    # remove() 方法
    list3.remove('pear')
    list3.remove(["Litchi","potato"])
    print("remove = ",list3)

    # insert()方法
    list3.insert(0,'pear')
    
    # reverse() 方法
    list3.reverse()
    print("reverse = ",list3)

    # sort() 方法
    list3.sort()
    print('sort =',list3)


if __name__ == "__main__":
    listTest()
