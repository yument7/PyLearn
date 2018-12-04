#!/usr/bin/python3
# --codind=utf-8--

import time

# 字符串定义以及相关字符串操作符测试
def strTest():
    str1 = 'hello'
    str2 = "world"
    str = str1 + str2
    print("the operator of '+' test:%s"%str)
    print("the operator of '[]' test:%s"%str[5])
    print("the operator of '[:]' test:%s"%str[1:7])
    print("the operator of 'in' test:%s"%('a' in str))
    print("the operator of 'not in' test:%s"%('a' not in str))
    
# 字符串相关操作方法
def operatorMethodTest():
    # find(substring[,start[,end]])
    sentence = "hello world,this is a apple."
    print('find=%s'%sentence.find("a"))
    print('rfind=%s'%sentence.rfind("a"))
    # replace(old,new[,max]) max代表替换次数 ，会返回一个新字符串
    print(sentence.replace("hello","hi"))

# 字符串与日期 需使用time 模块
def strAndTimeTest():
    pass

if __name__ == "__main__":
    strTest()
