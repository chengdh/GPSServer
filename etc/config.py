#coding=utf-8
#,YouWeiServerFactory,YaxunServerFactory

dic={}
#请按照配置文档说明配置 不要试图写入错误的值
# serverPort－TCP服务的端口号
# factory－创建与设备的TCP链接的工厂类 (只要不是新种类的设备无须修改 方便后台调用)
# mysqlHost，mysqlUser，mysqlPasswd－要连接的 Mysql 服务器的 主机名（本地的话 就写localhost），用户名，密码
# enable－是否启用 True是启用 False是废弃
#
#gpsTableClearTime对unpn数据库内的gps表做定时清理
#almTableClearTime对unpn数据库内的alm表做定时清理
gpsTableClearTime=1
almTableClearTime=1
#------------------------------------------------------------------------#
dic['simple_factory']={ 'serverPort':5010,
    'factory': "simple_factory.SimpleFactory()",
    'mysqlHost':'localhost',
    'mysqlUser':'root',
    'mysqlPasswd':'antongroot',
    'db':'unpn',
    'unpn_history':'unpnhis',
    'enable':True}


dic['TianHe']={ 'serverPort':5010,
    'factory': "TianHeServerFactory.TianHeFactory()",
    'mysqlHost':'localhost',
    'mysqlUser':'root',
    'mysqlPasswd':'antongroot',
    'db':'unpn',
    'unpn_history':'unpnhis',
    'enable':True}

dic['test']={ 'serverPort':6000,
    'factory': "TianHeServerFactory.TianHeFactory()",
    'mysqlHost':'localhost',
    'mysqlUser':'root',
    'mysqlPasswd':'antongroot',
    'db':'unpn_test',
    'unpn_history':'testhis',
    'enable':True}
'''

dic['YouWei']={ 'serverPort':6969,
    'factory':YouWeiServerFactory.YouWeiFactory(),
    'mysqlHost':'localhost',
    'mysqlUser':'root',
    'mysqlPasswd':'antongroot',
    'db':'myPythonServerTestdb',
    'unpn_history':'unpnhis',
    'enable':False}
dic['Yaxun']={ 'serverPort':9008,
    'factory':YaxunServerFactory.YaxunFactory(),
    'mysqlHost':'localhost',
    'mysqlUser':'root',
    'mysqlPasswd':'antongroot',
    'db':'myPythonServerTestdb',
    'unpn_history':'unpnhis',
    'enable':True}
'''
