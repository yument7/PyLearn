#!/usr/bin/python3
# --codind=utf-8--

def numberTest():
    int_a=10
    float_a=10.54
    bool_a=True
    complex_a=4+5j
    type_int = type(int_a)
    type_float = type(float_a)
    type_bool = type(bool_a)
    type_complex = type(complex_a)
    print("the type of int_a：%s"%type_int)
    print("the type of float_a：%s"%type_float)
    print("the type of bool_a：%s"%type_bool)
    print("the type of complex_a：%s"%type_complex)

# 算术运算符
def arithmeticOperatorTest():
    sum_plus = 10+10.0
    sum_subtract = 12-10.0
    sum_multiply = 12*10.0
    sum_divide = 12/5
    sum_remainder = 17%4
    sum_round = 17//3
    sum_square = 10**2
    print("[plus=%d,subtract=%d,multiply=%d,divide=%d,remainder=%d,round=%d,square=%d]"\
    %(sum_plus,sum_subtract,sum_multiply,sum_divide,sum_remainder,sum_round,sum_square))  

# 赋值运算符
def assignmentOperatorTest():
    a = 2
    b = 5.0
    sum_a = 0
    sum_a += a
    sum_a *= b
    sum_a -= a
    sum_a /= a
    sum_a %= b
    sum_a //= a
    sum_a **= a
    print('sum_a=%d'%sum_a)

# 位运算符
def bitOperatorTest():
    num1 = 2 & 4
    num2 = 2 | 5
    num3 = 2 ^ 7
    num4 = ~ 9
    num5 = 5 << 2     # <=> 5 * 2^2
    num6 = 100 >> 2   # <=> 100 * 2^-2
    print("[num1=%d,num2=%d,num3=%d,num4=%d,num5=%d,num6=%d]"\
    %(num1,num2,num3,num4,num5,num6))

if __name__ == "__main__":
    test = input('please input zhe order :(1=number,2=arithmetic,3=assignment,4=bit)\n :')
    test = int(test)
    if test == 1:
        numberTest()
    elif test == 2:
        arithmeticOperatorTest()
    elif test == 3:
       assignmentOperatorTest()
    elif test == 4:
        bitOperatorTest()