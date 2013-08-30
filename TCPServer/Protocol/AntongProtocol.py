# encoding:utf-8
from twisted.internet import protocol, reactor
from twisted.python import log
import MySQLdb
import datetime
import random
import struct
import time
from TCPServer.SqlOpration import SqlOprate 

def convert_lat_lon(v):
    """
    转换经度纬度
    ddmmmmmm --> d
    要求 v 是整数
    """
    return round(int(v/1000000) + float(v % 1000000) / 600000, 6)



class AntongProtocol(protocol.Protocol):
    #databuffer为缓冲区
    databuffer = ''
    timeOut=330
    timeout_deferred=None
    #当前连接设备id
    epidCurrent=None
    
    connected=False

    def __init__(self, factory):
        self.factory = factory
    
    def connectionMade(self):
        log.msg("connection")
        self.factory.numProtocols = self.factory.numProtocols+1
        log.msg(self.factory.numProtocols)
        #设置超时
        self.timeout_deferred = reactor.callLater(30, self.timeout)
        connected=True

    def timeout(self):
        '''
        超时设置
        '''
        if self.epidCurrent:
            log.msg(self.epidCurrent+"--timeout")
            now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
            value=(now,self.epidCurrent)
            #SqlOprate.sqlUpdate_epstatLost(self.factory.factoryKey,value)

        self.transport.loseConnection()
    
    def connectionLost(self, reason):
        '''
        连接丢失
        '''
        log.msg("connectionLost")

        if self.epidCurrent:
            now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
            value=(now,self.epidCurrent)
            SqlOprate.sqlUpdate_epstatLost(self.factory.factoryKey,value)
 
        if self.factory.devepid.get(self.epidCurrent) == self:
            del self.factory.devepid[self.epidCurrent]
        
        if self.timeout_deferred.active():
            self.timeout_deferred.cancel()
            del self.timeout_deferred

        self.factory.numProtocols = self.factory.numProtocols-1
 
    
    def dataReceived(self, data):
        #重置超时设置
        if self.timeout_deferred:
            self.timeout_deferred.cancel()
            self.timeout_deferred = reactor.callLater(self.timeOut, self.timeout)
         
        self.frameReceived(data)

    #登录确认
    def sd_accept(self):
      utc_time = struct.pack('<i', int(time.time()))
      accept_login_data=''.join([
        "\x7e",     #帧头1 7E
        "\xfe",     #帧头2 FE
        "\x20",     #协议版本 
        "\x40",     #帧号 0x40 接受登录
        "\x13\x00", #帧数据长度
        utc_time,   #utctime uint32
        '\x06',     #终端名称长度    
        'antong'    #终端名称
        '\x07'      #文本信息长度
        'welcome',  #文本信息
        "\x0d",     #帧尾
        ])
      log.msg('SD_ACCEPT : %s' % repr(accept_login_data))
      self.transport.write(accept_login_data)


    def frameReceived(self,data):
        #判断帧号
        frame_no = data[3]

        if frame_no == '\x20':
          epid_no = data[6:10] 
          epid,=struct.unpack('i',epid_no)
          self.epidCurrent =str(epid)
          log.msg("DS_LOGIN : %s" % repr(data) )
          log.msg("DS_LOGIN epid =  %s" %epid )
          self.sd_accept()

        #发送终端信息
        #DS_INFO
        if frame_no == '\x01':
          log.msg('DS_INFO: %s' % repr(data))

        #设置心跳
        #DS_SET_HEART
        if frame_no == '\x24':
          log.msg('DS_SET_HEART : %s' % repr(data))

        #发送GPS信息
        #DS_FINISH
        if frame_no == '\x21':
          log.msg('DS_GPS: %s' % repr(data))
          gps_info = [utc_time,lat,lon,direction,speed,miles] = struct.unpack('iiihhi',data[6:26])
          log.msg('parsed gps epid: %s info = %s' % (self.epidCurrent,repr(gps_info)))

          #DS_FINISH
          finish_flag = data[-11:][3]
          if finish_flag == '\x26':
            log.msg('DS_FINISH')
            finish_flag_data="\x7e\xfe\x20\x58\x04\x00\x10\x00\x00\x00\x0d"
            log.msg('SD_FINISH')
            self.transport.write(finish_flag_data)

          #更新数据库
          #插入ep表
          #epid,devtype,bankno,name,dept_id,creator_id
          key = devtype =  self.factory.factoryKey
          v_1 = ('NULL',self.epidCurrent,devtype)
          now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")

          SqlOprate.sqlInsert_ep(key,v_1)
          #插入gps表
          #('NULL',epid,now,t,jingdu,weidu,direction,speedD,0,state)
          v_2 = ('NULL',self.epidCurrent,now,now,convert_lat_lon(lat),convert_lat_lon(lon),direction,speed,0,'NULL')
          SqlOprate.sqlInsert_gps(key,v_2)
          #插入或更新epstat表
          v_3 = v_2 + v_2[2:]
          SqlOprate.sqlInsert_epstat(key,v_3)
