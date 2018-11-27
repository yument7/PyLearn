#!/usr/bin/python3
# --codind=utf-8--

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
    
if __name__ == "__main__":
    strTest()
