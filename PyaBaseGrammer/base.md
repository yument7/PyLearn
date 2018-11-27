1. python文件类型
   源代码文件    .py
   字节码文件    .pyc
   优化代码文件  .pyo

2. python编码规范
   标识符： 
        以 _ 或字母开头，后接任意数量下划线、字母和数字；
        禁止使用 Python 保留字（或关键字）
   
      ① 变量名、包名、模块名： 通常采用小写，可使用下划线
   
      ② 类名、对象名：类名首字母大写，对象名采用小写；
                类的私用属性、私用属性以两个下划线作为前缀；
                单下划线做前缀的属性和方法，from import 无法引用。
   
      ③ 函数名：通常采用小写，导入的函数以模块名做前缀。

   注释：
        单行注释： #开头
        多行注释： ''' ''' 三引号
        中文注释： 需要添加语句 # coding=UTF-8

   语句：
    一条语句多行显示：
        使用 \ 完成一条语句多行显示
        eg. sum = num_1 +\
                  num_2
    
    一行显示多条语句：
        多条语句使用 ; 隔开
        eg. a=10; b=20; c=30;
    
3. 输入输出
   输入语句： input()
   输出语句： print()          

4. 数据类型
   Number-数字类型  String-字符串类型  Tuple-元组类型  List-列表类型  Dictionary-字典类型  Sets-集合类型
   
   4.1 Number
       int-整型  long-长整型  float-浮点类型  bool-布尔类型  complex-复数类型

   4.2 String
       单引号与双引号  三引号  转义字符   

   4.3 Tuple
       创建：tp1 = (1,2,3) ,tp2 = ('abcd'), tp2 = tuple(['a','b','c'])
       
       访问：tp1 = (1,2) , tp1[2]   

   4.4 List
       创建： list1 = [1,2,3,4,5] , list2 = list(('a','b','c','d'))

       访问： list1[0] list1[1:3] 

       赋值： x = [1,2,3] , x[2] = 5 

       元素删除：del x[2]

       列表分片赋值：x = list1[1:3]

       列表常用方法：append() count() extend() reverse() remove() sort()
       
   4.5 Dictionary
       格式：d = {key1:value1,key2:value2}

       创建：d1 = dict([('name','li'),('sex','male')]) , d2 = {name:li,age:20,sex:male} , d3 = {} 

       访问：value = dict[key] 

       赋值：dict['x'] = value

       常用方法：dict() clear() pop() get() keys() values() update()

       全局字典： sys.modules模块

   4.6 Sets  集合中元素是无序的
       创建：s1 = set('python') ,s2 = set((1,2,3)), s3 = set([1,2,3]), s4 = {1,2,3,4} ,s5 = set() 

       常用方法：add() update() remove() 

       集合运算符操作： == != < > >= <= | & -

   4.7 序列
       能通过索引访问的数据类型都是序列，即字符串，元组，列表

2. 运算符与表达式
   算术运算符与表达式       [ +, -, *, /, %, //, ** ]
   关系运算符与表达式       [ ==, !=, <>, >, <, >=, <= ]
   逻辑运算符与表大式       [ and, or, not ]
   位运算符与表达式         [ &, |, ^, ~, <<, >> ]
   赋值运算符与表达式       [ =, +=, -=, *=, /=, %=, //=, **= ]
   字符串运算符与表达式     [ +, [], [:], in, not in, % ]

3. 常用函数
   类型转换常用函数        int(x) float(x) str(x) chr(x) ord(x) hex(x) oct(x) tuple(s) list(s) set(s) dict(d)
   数学常用函数            abs(x) fabs(x) ceil(x) floor(x) pow(x,y) exp(x) sqrt(x) log10(x) log(x[,y]) sin(x) cos(x) tan(x)
   字符串常用函数          capitalize() lower() upper() title() count(x) index(s) find(s) encode(coding) split(delimter) join()