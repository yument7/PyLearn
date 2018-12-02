一、 函数

1.函数定义
  Python 使用 def 关键字定义函数
  形式： 
    def functionName():
        statements
        return expression
  eg. 定义一个空函数
    def nothingFn():
        pass    # 以pass 关键为内容体

2.函数调用
    funcitonName(args ...)

3.函数嵌套
    函数中可以再定义函数，外部函数调用，内部函数也会被调用执行

4.函数递归调用
    fac(n) = 1 n=1
           = n*fac(n-1) n > 1
  两个条件：
    ①. 给出递归终止的条件和相应的状态（结果），fac函数递归终止条件为 n = 1, 结果状态：fac(1) = 1
    ②. 给出递归的表述形式，并且要向着终止条件变化，在有限的步骤内到达终止条件。

5.变量作用域

二、模块

1.导入与创建模块
  导入：
      通过 import 关键字导入，格式如下：
      import module1[,module2[,...moduleN]]
      
      只引入模块中某个函数，格式如下：
      from modulName import name1[,name2[,..nameN]]

  创建模块：
      每一个Python文件都可以作为一个模块，模块的名字就是文件的名字。

2.模块包
  包（package）用来组织模块的一个目录，类似java 的package
  
  让Python把一个目录当做包，该目录下必须有__init__.py文件，该文件可以是空文件，但文件必须存在。
  
  从包中导入模块，格式如下：
  import PackageA.SubPackageA.ModuleA
  from PackageA.SubPackageA import ModuleA as mda
