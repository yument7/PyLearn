#!/usr/bin/python3

# --coding=UTF-8--
# 使用递归方法，逆序打印出输入的字符串，字符串长度固定为5，例如abcde

def inputOutputTest(n):
    str=input('请输入字符：')
    if n==1:
      return str    
    else:
      return inputOutputTest(n-1)+str
        
if __name__ == "__main__":
    str = inputOutputTest(5)
    print('the reverse str is: %s'%str)



