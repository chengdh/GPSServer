# encoding:utf-8
from twisted.internet import protocol, reactor
from twisted.python import log
import MySQLdb
import datetime
import struct
from SqlOpration import SqlOprate 
import random
import struct
import time


ST_3746 = struct.Struct(">BBBIHB 3B3B H 4s4s BB BHBB")

if True:
    yaxun_ord = ord
    yaxun_7to8 = lambda s: s
    yaxun_8to7 = lambda s: s
else:
    def yaxun_8to7(data):
        """8/7 编码
        """
        if isinstance(data, basestring):
            data = bytearray(data)
        div, mod = divmod(len(data), 7)
        out = bytearray()
        for i in xrange(div):
            n = i * 7
            s = data[n:n + 7]
            out.extend((
                s[0] >> 1,
                ((s[0] << 6) + (s[1] >> 2)) & 0x7f,
                ((s[1] << 5) + (s[2] >> 3)) & 0x7f,
                ((s[2] << 4) + (s[3] >> 4)) & 0x7f,
                ((s[3] << 3) + (s[4] >> 5)) & 0x7f,
                ((s[4] << 2) + (s[5] >> 6)) & 0x7f,
                ((s[5] << 1) + (s[6] >> 7)) & 0x7f,
            ))
        if mod:
            s = data[-mod:]
            if mod == 1:
                out.extend((
                    s[0] >> 1,
                    ((s[0] << 6)) & 0x7f,
                ))
            elif mod == 2:
                out.extend((
                    s[0] >> 1,
                    ((s[0] << 6) + (s[1] >> 2)) & 0x7f,
                    ((s[1] << 5)) & 0x7f,
                ))
            elif mod == 3:
                out.extend((
                    s[0] >> 1,
                    ((s[0] << 6) + (s[1] >> 2)) & 0x7f,
                    ((s[1] << 5) + (s[2] >> 3)) & 0x7f,
                    ((s[2] << 4)) & 0x7f,
                ))
            elif mod == 4:
                out.extend((
                    s[0] >> 1,
                    ((s[0] << 6) + (s[1] >> 2)) & 0x7f,
                    ((s[1] << 5) + (s[2] >> 3)) & 0x7f,
                    ((s[2] << 4) + (s[3] >> 4)) & 0x7f,
                    ((s[3] << 3)) & 0x7f,
                ))
            elif mod == 5:
                out.extend((
                    s[0] >> 1,
                    ((s[0] << 6) + (s[1] >> 2)) & 0x7f,
                    ((s[1] << 5) + (s[2] >> 3)) & 0x7f,
                    ((s[2] << 4) + (s[3] >> 4)) & 0x7f,
                    ((s[3] << 3) + (s[4] >> 5)) & 0x7f,
                    ((s[4] << 2)) & 0x7f,
                ))
            elif mod == 6:
                out.extend((
                    s[0] >> 1,
                    ((s[0] << 6) + (s[1] >> 2)) & 0x7f,
                    ((s[1] << 5) + (s[2] >> 3)) & 0x7f,
                    ((s[2] << 4) + (s[3] >> 4)) & 0x7f,
                    ((s[3] << 3) + (s[4] >> 5)) & 0x7f,
                    ((s[4] << 2) + (s[5] >> 6)) & 0x7f,
                    ((s[5] << 1)) & 0x7f,
                ))
    
        return str(out)
    
    def yaxun_7to8(data):
        """
        7/8 解码
        @type data: bytearray
        @param data: 需要解码的数据
        """
        if isinstance(data, basestring):
            data = bytearray(data)
        div, mod = divmod(len(data), 8)
        out = bytearray()
        for i in xrange(div):
            n = i * 8
            s = data[n:n + 8]
            out.extend((
                (s[0] << 1) % 0x100 + (s[1] >> 6),
                (s[1] << 2) % 0x100 + (s[2] >> 5),
                (s[2] << 3) % 0x100 + (s[3] >> 4),
                (s[3] << 4) % 0x100 + (s[4] >> 3),
                (s[4] << 5) % 0x100 + (s[5] >> 2),
                (s[5] << 6) % 0x100 + (s[6] >> 1),
                (s[6] << 7) % 0x100 + (s[7]),
            ))
        if mod:
            s = data[-mod:]
            if mod == 2:
                out.extend((
                    (s[0] << 1) % 0x100 + (s[1] >> 6),
                ))
            elif mod == 3:
                out.extend((
                    (s[0] << 1) % 0x100 + (s[1] >> 6),
                    (s[1] << 2) % 0x100 + (s[2] >> 5),
                ))
            elif mod == 4:
                out.extend((
                    (s[0] << 1) % 0x100 + (s[1] >> 6),
                    (s[1] << 2) % 0x100 + (s[2] >> 5),
                    (s[2] << 3) % 0x100 + (s[3] >> 4),
                ))
            elif mod == 5:
                out.extend((
                    (s[0] << 1) % 0x100 + (s[1] >> 6),
                    (s[1] << 2) % 0x100 + (s[2] >> 5),
                    (s[2] << 3) % 0x100 + (s[3] >> 4),
                    (s[3] << 4) % 0x100 + (s[4] >> 3),
                ))
            elif mod == 6:
                out.extend((
                    (s[0] << 1) % 0x100 + (s[1] >> 6),
                    (s[1] << 2) % 0x100 + (s[2] >> 5),
                    (s[2] << 3) % 0x100 + (s[3] >> 4),
                    (s[3] << 4) % 0x100 + (s[4] >> 3),
                    (s[4] << 5) % 0x100 + (s[5] >> 2),
                ))
            elif mod == 7:
                out.extend((
                    (s[0] << 1) % 0x100 + (s[1] >> 6),
                    (s[1] << 2) % 0x100 + (s[2] >> 5),
                    (s[2] << 3) % 0x100 + (s[3] >> 4),
                    (s[3] << 4) % 0x100 + (s[4] >> 3),
                    (s[4] << 5) % 0x100 + (s[5] >> 2),
                    (s[5] << 6) % 0x100 + (s[6] >> 1),
                ))
            else:
                pass
    
        return str(out)
    
    def yaxun_ord(c):
        """
        编码时：如字节为 0，则转义为 7FH，这里是解码
        """
        if c == "\x7f":
            return 0
        return ord(c)


def yaxun_checksum(checksum):
    """
    带进位累加和 -- 校验和，然后"雅迅"一下
    用法:
        yaxun_checksum(sum(bytearray(data)))
    """
    return (checksum / 0x100 + (checksum & 0xff)) & 0xff

def yaxun_coordinate(c):
    try:
        d = ord(c[0])
        f1, f2, f3 = map(yaxun_ord, c[1:])
        f = f1 * 10000 + f2 * 100 + f3
        return round(d + f / 600000.0, 6)
    except Exception as e:
        log.err(e)


class YaxunProtocol(protocol.Protocol):
    
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
        if self.factory.devepid.get(self.epidCurrent) == self:
            del self.factory.devepid[self.epidCurrent]
        
        if self.timeout_deferred.active():
            self.timeout_deferred.cancel()
            del self.timeout_deferred

        self.factory.numProtocols = self.factory.numProtocols-1
 
    
    def dataReceived(self, data):
        log.msg("dataReceived format = %s" % " ".join(["%02x" % c for c in bytearray(data)]))
        log.msg("dataReceived = %s" % repr(data))

        #重置超时设置
        if self.timeout_deferred:  
            self.timeout_deferred.cancel()  
            self.timeout_deferred = reactor.callLater(self.timeOut, self.timeout)  

        '''
        暂时注释,只处理一帧的情况
 
        self.databuffer += data

        while self.databuffer:
            if not self.databuffer.startswith("\x7e"):
                log.msg("discard: %s" % repr(self.databuffer))
                self.databuffer = ""
                break

            pos = self.databuffer.find("\x7e", 1)
            if pos == -1:
                break

            self.frameReceived(self.databuffer[1:pos])
            self.databuffer = self.databuffer[pos + 1:]
        '''
        self.parse_data(data)

    def  parse_data(self,data):
        #判断帧号
        frame_no = data[3]
        log.msg("frame no=%s" % repr(frame_no))
        if frame_no == '\x20':
          log.msg("this is login")
          self.accept_login()
        if frame_no == '\x21':
          log.msg('this is sended gps info')
          self.parse_gps_info(data)
    
    def accept_login(self):
      '''
      登录确认
      '''
      data = "\x7e\xfe\x13\x40\x05\x01\x0f\x0f\x01ok\x0d"
      #data = "\x7e\xfe\x13\x40\x0b" + hex_utc_timestamp + "welcome\x0d"
      log.msg("accept_login")
      self.transport.write(data)

    def parse_gps_info(self,data):
      '''
      解析gps位置数据信息
      '''
      #|7E|FE|版本1|帧号1|帧数据长度2|utc时间（4位)|纬度4|经度4|方向2|速度2|累计里程4
      gps_info = {
          'utc_time' :data[6:10] ,
          'lat' :     data[10:14], 
          'lon' :     data[14:18],
          'direction':data[18:20],
          'speed':    data[20:22],
          'milles' :  data[22:],
          }
      log.msg('parse gps info = %s' % repr(gps_info))
      return gps_info

    def frameReceived(self, data):
        data = data.replace("\x7d\x00", "\x7d").replace("\x7d\x01", "\x7e")
        log.msg('in frameReceived data = %s' % repr(data))
        # 忽略校验和，好像设备上传的校验和不对
        version, checksum, priority, cmdno = map(ord, data[:4])
        data = data[4:]
        # 从版本号到数据字段的各个字节的带进位累加和
        real_checksum = yaxun_checksum(sum(bytearray(data)) + cmdno + priority + version)
        if cmdno == 0x01:
            usercode = data[:6]
            argc = ord(data[6])     # 应该总是 1
            arg1type = data[7]
            arg1len = ord(data[8])
            arg1 = data[9:9 + arg1len - 1]
            if arg1type != "\x01":
                return log.msg("error arg1type: %r" % arg1type)
            self.epidCurrent = arg1.rstrip(" ")
            #self.repstr = devid
            #self.pauseProducing()
            #self.loadConfig()
            self.sendFrame(0x81, "\x01", version, priority)
        elif cmdno == 0x02:
            checksum = ord(data[-1])
            real_checksum = yaxun_checksum(sum(bytearray(data[:-1]))) & 0x7f
            #区域号: 2
            #版本号: 2  0x1070
            svctype = ord(data[4])
            datatype = ord(data[5])
            data = data[6:-1]
            # 带进位累加和，累加完后将该字节最高位清零，如最终结果为 0，则转义为 7FH。
            log.msg("t:{0:02x}{1:02x} c:{2:02x} rc:{3:02x}".format(svctype, datatype, checksum, real_checksum))
            datatype = svctype * 0x100 + datatype
            if datatype == 0x3746:
                data = yaxun_7to8(data)
                (answer, win, seqno, milage, interval,
                    gpscount, Y, m, d, H, M, S, driver,
                    latitude, longitude, speed, direction,
                    sensor_stat, stat, alm_sensor_stat,
                    load_sensor_count) = ST_3746.unpack_from(data)
                extra = data[ST_3746.size:]
                Y += 2000
                latitude = yaxun_coordinate(latitude)
                longitude = yaxun_coordinate(longitude)
                speed = round(speed * 1.852, 1)
                _W, _T, A = (answer >> 3) & 0x01, (answer >> 1) & 0x01, answer & 0x01
                log.msg("3746", bin(answer), win, seqno, milage, interval,
                    gpscount, Y, m, d, H, M, S, driver,
                    latitude, longitude, speed, direction,
                    sensor_stat, stat, alm_sensor_stat,
                    load_sensor_count), repr(extra)
                if A:
                    self.send83(0x37, 0x06, "\x01")

            elif datatype == 0x0154:
                log.msg('WARNING: {0:04x} {1} {2!r}'.format(datatype, len(data), data))
            else:
                log.msg('TODO: {0:04x} {1} {2!r}'.format(datatype, len(data), data))

    def sendFrame(self, cmdno, data, version=0, priority=0x04):
        checksum = yaxun_checksum(sum(bytearray(data)) + cmdno + version + priority)
        data = ''.join([
            chr(version),
            chr(checksum),
            chr(priority),
            chr(cmdno),
            data
        ])
        data = data\
            .replace("\x7d", "\x7d\x00")\
            .replace("\x7e", "\x7d\x01")
        self.write("\x7e" + data + "\x7e")

    def send83(self, svctype, datatype, data, version=0x03, priority=0x04):
        data = "".join((
            "\x11\x22",
            "\x10\x70",
            chr(svctype),
            chr(datatype),
            self.epidCurrent.ljust(15, " "),
            "13800000000".ljust(15, " "),
            yaxun_8to7(data),
        ))
        checksum = yaxun_checksum(sum(bytearray(data)))
        if checksum == 0:
            checksum = 0x7f
        self.sendFrame(0x83, data + chr(checksum), version, priority)

    def send84(self, interval=5):
        self.sendFrame(0x84, chr(interval))
