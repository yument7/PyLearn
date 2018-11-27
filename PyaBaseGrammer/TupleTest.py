#!/usr/bin/python3
# --coding=UTF-8--

def tupleTest():
    tp1 = (1,2,3,4,5)
    # tp1[2] = 9  错误的，不允许通过索引修改元组的值
    tp2 = tuple(['apple','oragne','banner','pear','peach','grape'])
    print("tp1=%s,tp1[2]=%s"%(tp1,tp1[2]))
    # print("tp2[1:5]=%s"%(tp2[1:5])) 错误的， 元组没有切片功能

    list1 = list(tp2)
    print(list1)
    x = list1.sort() 
    # tp2 = tuple(list1.sort()) 错误调用，list1.sort()
    tp2 = tuple(list1)
    print(x)
    print("sorted tuple tp2 =",tp2)

if __name__ == "__main__":
    tupleTest()