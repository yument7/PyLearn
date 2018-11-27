#!/usr/bin/python3
# --coding=UTF-8--
import math

# 类型转换常用函数
def typeConversionMethod():
    int_x = int('10')
    float_x = float('10.50')
    str_x = str(10.55)
    chr_x = chr(65)
    ord_x = ord('a')
    hex_x = hex(124)
    oct_x = oct(73)
    tuple_x = tuple([1,2,3,4])
    list_x = list(('a','b','c','d'))
    set_x = set([(1,2),(3,4),(5,6)])
    dict_x = dict([('name','li'),('sex','female'),('age','24')])
    
    print("int_x=%d,float_x=%s,str_x=%s,chr_x=%s,ord_x=%s,hex_x=%s,oct_x=%s"%\
    (int_x,float_x,str_x,chr_x,ord_x,hex_x,oct_x))
    print("tuple_x=%s,list_x=%s,set_x=%s,dict_x=%s"\
    %(tuple_x,list_x,set_x,dict_x))

# 常用数学函数
def mathMethod():
    abs_x = abs(-10)
    fabs_x = math.fabs(-34)
    ceil_x = math.ceil(1.66)
    floor_x = math.floor(1.55)
    pow_x = math.pow(2,10)
    exp_x = math.exp(2)
    sqrt_x = math.sqrt(100)
    log_x = math.log10(100)
    ln_x = math.log(exp_x)
    sin_x = math.sin(math.pi/6)
    cos_x = math.cos(math.pi/3)
    tan_x = math.tan(math.pi/4)
    print("abs_x=%d,fabs_x=%d,ceil_x=%s,floor_x=%s,pow_x=%s,exp_x=%s,sqrt_x=%s,log_x=%s,ln_x=%s,sin_x=%s,cos_x=%s,tan_x=%s"\
    %(abs_x,fabs_x,ceil_x,floor_x,pow_x,exp_x,sqrt_x,log_x,ln_x,sin_x,cos_x,tan_x))

# 常用字符串函数
def StringMethod():
    string = "life is short so i chose python"
    str1 = string.capitalize()
    str2 = string.count('i')
    str3 = string.index('so')
    str4 = string.find('so')
    str5 = string.lower()
    str6 = string.upper()
    str7 = string.title()
    str8 = string.split(' ')
    str9 = ' '.join(['i','love','you'])
    str10 = string.encode('utf-8')
    print('%s, %s ,%s ,%s, %s, %s, %s, %s, %s, %s'%\
    (str1,str2,str3,str4,str5,str6,str7,str8,str9,str10))
    
if __name__ == "__main__":
    test = input("chose: 1,2,3 \n")
    test = int(test)
    
    if test == 1:
        typeConversionMethod()
    elif test == 2:
        mathMethod()
    elif test == 3:
        StringMethod()
    else:
        print('nothing')