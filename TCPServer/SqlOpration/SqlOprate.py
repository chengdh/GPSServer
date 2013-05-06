#coding=utf-8
from twisted.python import log
import MySQLdb
import datetime
import math

SQL_Connection={}
HistroySQL_Connection={}
gpsClearDay=1
almClearDay=1
LastGpsTime=datetime.datetime(2012,12,12)
LastAlmTime=datetime.datetime.now()
#更新gps清理间隔单位：天
def updateGpsClearDay(day):
    global gpsClearDay
    gpsClearDay=day

#更新alm清理间隔单位：天
def updateAlmClearDay(day):
    global almClearDay
    almClearDay=day

#unpn连接
def sqlUnpnConnect(key,dic):
    try:
        conn = MySQLdb.connect(host=dic['mysqlHost'], user=dic['mysqlUser'],passwd=dic['mysqlPasswd'] ,db=dic['db'],charset='utf8')
        cursor = conn.cursor()
        SQL_Connection[key]={'mysqlConnection':conn,'mysqlCursor':cursor}

    except MySQLdb.Error,e:
            log.err()

#unpn_histroy连接
def sqlUnpnhisConnect(key,dic):
    try:
        c=MySQLdb.connect(host=dic['mysqlHost'], user=dic['mysqlUser'],passwd=dic['mysqlPasswd'] ,db=dic['unpn_history'],charset='utf8')
        cur=c.cursor()
        HistroySQL_Connection[key]={'mysqlHisConnection':c,'mysqlHisCursor':cur}

    except MySQLdb.Error,e:
        log.err()

#断开unpn连接
def sqlLostUnpnConnect(key,connection,cursor):
    try:
        if key in SQL_Connection:
            if connection and cursor:
                cursor.close()
                connection.close()
                del SQL_Connection[key]
    except MySQLdb.Error,e:
        log.err()




#断开unpn_histroy连接
def sqlLostUnpnhisConnect(key,connection,cursor):
    try:
        if key in HistroySQL_Connection:

            if connection and cursor:
                cursor.close()
                connection.close()
                del HistroySQL_Connection[key]

    except MySQLdb.Error,e:
        log.err()

#获取db的连接
def get_connection(key,history_db=False):
  '''
  连接数据库
  @param history_db 是否连接历史库
  '''
  try:
    conn = cursor = None;
    if key not in SQL_Connection:
      cfg = global_config.dic[key]
      if history_db:
        sqlUnpnhisConnect(key,cfg)
      else:
        sqlUnpnConnect(key,cfg)

    dic=SQL_Connection[key]

    if history_db:
      conn=dic['mysqlHisConnection']
      cursor=dic['mysqlHisCursor']
    else:
      conn=dic['mysqlConnection']
      cursor=dic['mysqlCursor']

    #ret
    return (conn,cursor)

  except MySQLdb.Error,e:
    log.err()

#获取Unpn的连接
def sqlGetUnpnConnection(key):
  return get_connection(key)
#获取Unpnhis的连接
def sqlGetUnpnhisConnection(key):
  return get_connection(key,True)

#unpn 操作
def sqlSelect_ep(cursor):
  try:
    if cursor:
      sql='select epid from ep'
      count = cursor.execute(sql)
      return count
    return None
  except MySQLdb.Error,e:
    log.err()

#清空gps并把id字段数字重置
def sqlDelete_gps(cursor):
    try:
        if cursor:
            sql='truncate table gps'
            cursor.execute(sql)
    except MySQLdb.Error,e:
        log.err()
#清空alm并把id字段数字重置
def sqlDelete_alm(cursor):
    try:
        if cursor:
            sql='truncate table alm'
            cursor.execute(sql)
    except MySQLdb.Error,e:
        log.err()
#插入ep表
def sqlInsert_ep(key,value):
    try:
      conn,cursor = sqlGetUnpnConnection(key)
      if conn and cursor:
        count=sqlSelect_ep(cursor)
        count=count/1000

        bankno=math.floor(count)
        v=(bankno,0,0,0)
        value=value+v
        log.msg(sql)
        sql="insert ignore into ep(epid,devtype,bankno,name,dept_id,creator_id) values(%s,'%s',%s,%s,%s,%s)"%value[1:]
        cursor.execute(sql)
        conn.commit()
        b=int(bankno)
        return b

      return -1
    except MySQLdb.Error,e:
      log.err()
#插入epstat
def sqlInsert_epstat(key,value):
    try:
      conn,cursor = sqlGetUnpnConnection(key)
      if conn and cursor:
        log.msg(sql)
        sql= "insert into epstat(epid,`time`,`state`,`desc`,gpstime,longitude,latitude,direction,speed,mileage,flags) values(%s,'%s',0,'在线','%s',%s,%s,%s,%s,%s,'%s') on DUPLICATE KEY UPDATE `time`='%s',gpstime='%s',`state`=0,`desc`='在线',longitude=%s,latitude=%s,direction=%s,speed=%s,mileage=%s,flags='%s'" % value[1:]
        cursor.execute(sql)
        conn.commit()

    except MySQLdb.Error,e:
      log.err()

#掉线时更新对应设备epstat表
def sqlUpdate_epstatLost(key,value):
    try:
      conn,cursor = sqlGetUnpnConnection(key)
      if cursor:
        now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        sql="update epstat set time='%s',state=1,epstat.desc='离线' where epid=%s"%value
        cursor.execute(sql)
    except MySQLdb.Error,e:
      log.err()

#设备登录在epstat表更新或建立对应数据
def sqlUpdate_epstatConnecting(key,value):
    try:
      conn,cursor = sqlGetUnpnConnection(key)
      if conn and cursor:
        sql= "insert into epstat(epid,`time`,`state`,`desc`,gpstime,longitude,latitude,direction,speed,mileage,flags) values(%s,'%s',0,'在线','%s',%s,%s,%s,%s,%s,'%s') on DUPLICATE KEY UPDATE `time`='%s',gpstime='%s',`state`=0,`desc`='在线',longitude=%s,latitude=%s,direction=%s,speed=%s,mileage=%s,flags='%s'"%value[1:]
        cursor.execute(sql)
        conn.commit()
    except MySQLdb.Error,e:
      log.err()

#插入alm表其中包括对alm历史表的创建和插入
def sqlInsert_alm(key,value):
    try:
      conn,cursor = sqlGetUnpnConnection(key)
      if conn and cursor:
        now =datetime.datetime.now()
        global LastAlmTime
        if abs((now-LastAlmTime).days)>=almClearDay:
          sqlDelete_alm(cursor)
          LastAlmTime=now
        sql="insert into alm values(%s,%s,'%s',%s,%s,'%s','%s',%s,%s,%s,%s,%s,'%s')"%value
        cursor.execute(sql)
        conn.commit()

        sqlCreateTable_unpnhisAlm(key,value)

    except MySQLdb.Error,e:
      log.err()

#插入gps表其中包括对gps历史表的创建和插入
def sqlInsert_gps(key,value):
    try:
      conn,cursor = sqlGetUnpnConnection(key)
      now = datetime.datetime.now()
      global LastGpsTime
      if abs((now-LastGpsTime).days)>=gpsClearDay:
        sqlDelete_gps(cursor)
        LastGpsTime=now
      if conn and cursor:
        sql="insert into gps values(%s,%s,'%s','%s',%s,%s,%s,%s,%s,'%s')"%value
        cursor.execute(sql)
        conn.commit()

      bankno=sqlSelect_epbankno(key,value[1])
      if bankno == -1:
        vv=(value[0],value[1],key)
        bank=sqlInsert_ep(key,vv)
        if bank!=-1:
          sqlCreateTable_unpnhisGps(key,bank,value)
      else:
        sqlCreateTable_unpnhisGps(key,bankno,value)

    except MySQLdb.Error,e:
        log.err()

#查询ep表的bankno字段
def sqlSelect_epbankno(key,epid):
    try:
      conn,cursor = sqlGetUnpnConnection(key)
      if cursor:
        sql="select bankno from ep where epid=%s"%epid
        data=cursor.execute(sql)
        data = cursor.fetchone()
        if data:
          data=data[0]
          return data
      return -1
    except MySQLdb.Error,e:
      log.err()


#unpnhis 操作
#创建unpnhis  的 gps历史表 包括调用其插入命令
def sqlCreateTable_unpnhisGps(key,bankno,value):
    try:
      conn,cursor = sqlGetUnpnhisConnection(key)
      if conn and cursor:
        now=datetime.datetime.now().strftime("%y%m")
        bankno=str(bankno)
        tableName='gps_'+now+'_'+bankno
        if sqlSelectTableName_His(key,tableName):
          sql="CREATE TABLE %s (id int(10) unsigned NOT NULL AUTO_INCREMENT,epid char(20) CHARACTER SET latin1 NOT NULL,time datetime DEFAULT NULL,reptime datetime DEFAULT NULL,longitude double DEFAULT NULL,latitude double DEFAULT NULL,direction smallint(5) unsigned DEFAULT NULL,speed smallint(5) unsigned DEFAULT NULL,mileage double DEFAULT NULL,flags char(20) CHARACTER SET latin1 DEFAULT NULL,PRIMARY KEY (id),KEY epid (epid),KEY time (time)) ENGINE=MyISAM AUTO_INCREMENT=0 DEFAULT CHARSET=utf8"%tableName
          cursor.execute(sql)

        sqlInsert_gpsHis(key,tableName,value)
    except MySQLdb.Error,e:
      log.err()
#创建unpnhis的 alm历史表 包括调用其插入命令
def sqlCreateTable_unpnhisAlm(key,value):
    try:
      alm='alm'
      conn,cursor = sqlGetUnpnhisConnection(key)
      if conn and cursor:
        if sqlSelectTableName_His(key,alm):
          sql="CREATE TABLE %s (id int(10) unsigned NOT NULL AUTO_INCREMENT,epid varchar(20) NOT NULL,time datetime NOT NULL,reptime datetime DEFAULT NULL,type smallint(6) DEFAULT NULL,data varchar(100) DEFAULT NULL,gpstime datetime DEFAULT NULL,longitude double DEFAULT NULL,latitude double DEFAULT NULL,direction smallint(5) unsigned DEFAULT NULL,speed smallint(5) unsigned DEFAULT NULL,mileage double DEFAULT NULL,flags varchar(10) DEFAULT NULL,PRIMARY KEY (id),KEY epid (epid),KEY time (time),KEY type (type)) ENGINE=MyISAM AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;"%alm
          cursor.execute(sql)
        sqlInsert_almHis(key,value)

    except MySQLdb.Error,e:
      log.err()

#插入gps历史表
def sqlInsert_gpsHis(key,tableName,value):
    try:
      conn,cursor = sqlGetUnpnhisConnection(key)
      if conn and cursor:
        value=list(value)
        value.insert(0,tableName)
        value=tuple(value)
        sql="insert into %s values(%s,%s,'%s','%s',%s,%s,%s,%s,%s,'%s')"%value
        cursor.execute(sql)
        conn.commit()

    except MySQLdb.Error,e:
      log.err()
#插入alm历史表
def sqlInsert_almHis(key,value):
    try:
      conn,cursor = sqlGetUnpnhisConnection(key)
      if conn and cursor:
        sql="insert into alm values(%s,%s,'%s',%s,%s,'%s','%s',%s,%s,%s,%s,%s,'%s')"%value
        cursor.execute(sql)
        conn.commit()

    except MySQLdb.Error,e:
      log.err()

#查询历史数据库 判断表示否存在 如果存在说明不用创建 返回False否则返回True
def sqlSelectTableName_His(key,tableName):
    try:
      conn,cursor = sqlGetUnpnhisConnection(key)
      if cursor:
        sql="SHOW TABLES LIKE '%s'"%tableName
        data=cursor.execute(sql)
        if data==0:
          return True

        return False

    except MySQLdb.Error,e:
        log.err()

