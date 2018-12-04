#!/usr/bin/python3
# --coding=UTF-8--

# 顺序查找， 从数组中查找出对应值得索引
def sequentialSearch(goalList,n):
    index = -1
    lens = len(goalList)
    for pos in range(0,lens):
        if goalList[pos] == n :
            index = pos
            break
    return index

# 折半查找 ， 二分法
def binarySearch(goalList,low,high,n):
    index = -1
    mid = (low+high)//2
    if low < high:
        binarySearch(goalList,low,mid,n)
        binarySearch(goalList,mid+1,high,n)
        i = low
        while i < high:
            if goalList[i] == n :
                index = i
                break
            i += 1
        return index 

# 冒泡排序
def buddleSort(goalList):
    # 检测传入对象是否是数组，即列表
    sign = isinstance(goalList,list)
    if sign == False:
        return goalList   
    for j in range(len(goalList)):
        for i in range(len(goalList)-j-1):
            if goalList[i] > goalList[i+1]:
                temp = goalList[i]
                goalList[i] = goalList[i+1]
                goalList[i+1] = temp
    return goalList

# 选择排序
def selectionSort(goalList):
     # 检测传入对象是否是数组，即列表
    sign = isinstance(goalList,list)
    if sign == False:
        return goalList   
    for j in range(len(goalList)):
        k = j
        for i in range(j+1,len(goalList)):
            if goalList[k] > goalList[i] :
                temp = goalList[k]
                goalList[k] = goalList[i]
                goalList[i] = temp     
    return goalList

# 插入排序
def insertSort(goalList):
    # 检测传入对象是否是数组，即列表
    sign = isinstance(goalList,list)
    if sign == False:
        return goalList   
    for j in range(1,len(goalList)):
        target = goalList[j]
        i = j-1
        while goalList[i] > target and i > 0: # 无 && 符号 
            goalList[i+1] = goalList[i]
            i -= 1
        goalList[i+1] = target
    return goalList 

# 归并排序   
def mergeSort(goalList):
    if len(goalList) <= 1:
        return goalList
    mid = len(goalList)//2
    left = mergeSort(goalList[:mid])
    right = mergeSort(goalList[mid:])
    target = []
    i=j=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            target.append(left[i])       
            i=i+1
        else :
            target.append(right[j])
            j=j+1
    while i<len(left):
        target.append(left[i])
        i+=1
    while j<len(right):
        target.append(right[j])
        j+=1
    return target

# lambda 函数使用， 计算(x+y)*(m-n)
def lambdaFunc():
    x = 1; y = 2; m = 3; n =4
    sumx = lambda x, y : x + y
    print('sum=%s'%sumx)
    sub = lambda m, n : m - n
    print('sub=%s'%sub)
    return sumx(x,y)*sub(m,n)

# Generator 函数使用
def generatorFunc(n):
    for i in range(n):
        yield i
                       
if __name__ == "__main__":
    goalList = [1,2,23,12,7,16,34,25,11,19]
    low = 0; high = len(goalList) - 1;n = 7
    choose = input('please choose you options:\n [1.order find 2.binary find 3.buddle_sort 4.select_sort 5.insert_sort 6.merge_sort] \n')
    choose = int(choose)
    if choose == 1:
        index = sequentialSearch(goalList,n)
        print(index)
    elif choose == 2:
        index = binarySearch(goalList,low,high,n)
        print(index)
    elif choose == 3:
        sortArray = buddleSort(goalList)
        print(sortArray)
    elif choose == 4:
        sortArray = selectionSort(goalList)
        print(sortArray)
    elif choose == 5:
        sortArray = insertSort(goalList)
        print(sortArray)
    elif choose == 6:
        sortArray = mergeSort(goalList)
        print(sortArray)
    elif choose == 7:
        print(lambdaFunc())
    elif choose == 8:
        for i in generatorFunc(3):
            print(i)
        r = generatorFunc(4)    
        print(next(r))
        print(next(r))