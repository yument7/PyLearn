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
    
if __name__ == "__main__":
    numberTest()
