#coding=utf-8
from Factory import TianHeServerFactory,YouWeiServerFactory

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
dic['TianHe']={ 'serverPort':9008,
    'factory':TianHeServerFactory.TianHeFactory(),
    'mysqlHost':'localhost',
    'mysqlUser':'root',
    'mysqlPasswd':'antongroot',
    'db':'unpn',
    'unpn_history':'unpnhis',
    'enable':True}


dic['YouWei']={ 'serverPort':6969,
    'factory':YouWeiServerFactory.YouWeiFactory(),
    'mysqlHost':'localhost',
    'mysqlUser':'root',
    'mysqlPasswd':'antongroot',
    'db':'myPythonServerTestdb',
    'unpn_history':'unpnhis',
    'enable':False}

