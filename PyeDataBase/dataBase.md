# python 数据库的连接

一、访问关系性数据库
    Python 标准数据库接口为 Python DB-API，Python DB-API为开发人员提供了数据库应用编程接口；支持多种数据库类型的连接，比如常用的oracle，mysql等

  1.访问mysql数据库
    python2中使用mysqldb模块，python3中使用pymysql;
    PyMySQL 遵循 Python 数据库 API v2.0 规范，并包含了 pure-Python MySQL 客户端库.
    PyMySQL 安装方式：
    方式1：
            pip3 install PyMySQL
    方式2：
            git clone https://github.com/PyMySQL/PyMySQL
            cd PyMySQL/
            python3 setup.py install

  2.访问oracle数据库
    python访问oracle数据库需要安装cx_Oracle模块
    注意：不同版本的python对应不同的cx_Oracle版本
    cx_Oracle 安装方式：
    方式1：
            pip3 install cx_Oracle
    方式2：
            进入https://pypi.org/project/cx_Oracle下载对应版本
                
二、访问非关系性数据库Nosql数据库
 
 1.访问Redis数据库
 
 2.访问MongoDB数据库
