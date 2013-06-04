# encoding:utf-8
from twisted.internet import protocol,reactor
from twisted.python import log
import MySQLdb
import datetime
import struct
from TCPServer.SqlOpration import SqlOprate 

TD_8HOUR = datetime.timedelta(0, 28800)



#16进制转换为2进制
def bin(number): 
    m = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', 
        '4':'0100', '5':'0101', '6':'0110', '7':'0111', 
        '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 
        'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'} 
    s = number
    return ''.join(m[x] for x in s)

class YouWeiProtocol(protocol.Protocol):
    timeOut=330
    timeout_deferred=None
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
    
    def dataReceived(self, data):
        
        #重置超时设置
        if self.timeout_deferred:  
            self.timeout_deferred.cancel()  
            self.timeout_deferred = reactor.callLater(self.timeOut, self.timeout)  
        
        log.msg(data)
        
        if data.startswith("*"):
            textcmd, e, data = data.partition("#")
            
            if e != "#":
                return
            
            self.textCommandReceived(textcmd)
        
        elif data.startswith("$"):
            
            data=data.split("$")
            self.binaryCommandReceived(data)
        else:
            pass
    def timeout(self):
        if self.epidCurrent:
            log.msg(self.epidCurrent+"--timeout")
            now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
            value=(now,self.epidCurrent)

        self.transport.loseConnection()
    
    def connectionLost(self, reason):
        log.msg("connectionLost")
        if self.factory.devepid.get(self.epidCurrent) == self:
            del self.factory.devepid[self.epidCurrent]
        
        if self.timeout_deferred:  
            self.timeout_deferred.cancel()
            del self.timeout_deferred
        
        now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        value=(now,self.epidCurrent)
        SqlOprate.sqlUpdate_epstatLost(self.factory.factoryKey,value)
        self.factory.numProtocols = self.factory.numProtocols-1
    
    #解析＊开头的数据
    def textCommandReceived(self, data):
        
        data=data.split(",")
        
        
        if data[2]=='V1':
            l=float(data[5])
            w=float(data[7])
            self.epidCurrent=data[1]
            
            value=('NULL',data[1],self.factory.factoryKey)
            
            SqlOprate.sqlInsert_ep(self.factory.factoryKey,value)
            
            
            if data[2]=='V1' and self.connected:
                self.connected=False
                
                last_epid=self.factory.devepid.get(self.epidCurrent)
                
                self.factory.devepid[self.epidCurrent]=self
                
                if last_epid and last_epid != self:
                    last_epid.transport.loseConnection()
            
            dmy=data[11]
            
            day=int(dmy[0:2])
            month=int(dmy[2:4])
            year=int(dmy[4:])
            
            hms=data[3]
            hour=int(hms[0:2])
            minute=int(hms[2:4])
            second=int(hms[4:])
            year += 2000
            t=datetime.datetime(year, month, day, hour, minute, second) + TD_8HOUR
            t=t.strftime("%y-%m-%d %H:%M:%S")
            direction=data[10]
            speed=data[9]
            state=data[-1]
            #print(data)
            if (data[5]!="" and l!=0) and (data[7]!="" and w!=0):
                
                str1=state[:2]
                str2=state[2:4]
                str3=state[4:6]
                str4=state[6:]
                str1=bin(str1)
                str2=bin(str2)
                str3=bin(str3)
                str4=bin(str4)
                discrubes=[];
                almType=[];
                #红色按钮 维修报警
                if str2[5]=='0':
                    log.msg("warnning－－维修报警")
                    discrube='维修报警'
                    tm=4
                    almType.append(tm)
                    discrubes.append(discrube)
                
                #绿色按钮 油料报警
                if str3[3]=='0':
                    log.msg("warnning－－油料报警")
                    discrube='油料报警'
                    tm=5
                    almType.append(tm)
                    discrubes.append(discrube)
                
                weidu=float(data[5])/100
                weidu=round(weidu,6)
                jingdu=float(data[7])/100
                jingdu=round(jingdu,6)
                
                for d in range(0,len(discrubes)):
                    now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                    value=('NULL',data[1],now,'NULL',almType[d],discrubes[d],t,jingdu,weidu,direction,speed,0,state)
                    SqlOprate.sqlInsert_alm(self.factory.factoryKey,value)
                    
                now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                value=('NULL',data[1],now,t,jingdu,weidu,direction,speed,0,state)
                value=value+value[2:]
                SqlOprate.sqlInsert_epstat(self.factory.factoryKey,value)
            else:
                now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
                value=('NULL',data[1],now,t,data[5],data[7],direction,speed,0,state)
                value=value+value[2:]
                SqlOprate.sqlInsert_epstat(self.factory.factoryKey,value)
    
    
    #解析$开头的2进制数据
    def binaryCommandReceived(self,data):
        #print(data)
        insetOrUpate=True
        end=len(data)
        #print(len(data))
        # print(end)
        for i in range(0,end):
            #插入表gps
            
            dataAtIndex=data[i]
            if len(dataAtIndex)==31:
                value=self.binaryCommandTransport(dataAtIndex)
                #print(value)
                if value[4]!=0 and value[5]!=0:
                    #print(value)
                    SqlOprate.sqlInsert_gps(self.factory.factoryKey,value)
                
                if insetOrUpate:
                    if len(data[end-i])==31:
                        value=self.binaryCommandTransport(data[end-i])
                        value=value+value[2:]
                        SqlOprate.sqlUpdate_epstatConnecting(self.factory.factoryKey,value)
                        insetOrUpate=False
    
    
    def binaryCommandTransport(self,data):
        (epid,eptime,epdate,weidu,bl0,jingdu,speedD,state,userAlarm,bl1,rNum)=struct.unpack('5s3s3s4sB5s3s4sBBB',data)
        epid=epid.encode("hex")
        eptime=eptime.encode("hex")
        epdate=epdate.encode("hex")
        weidu=float(weidu.encode("hex"))
        #bl0=bl0.encode("hex")
        jingdu=jingdu.encode("hex")  
        speedD=speedD.encode("hex")
        direction=speedD[3:]
        speedD=speedD[:3]
        
        state= state.encode("hex").upper()
        
        weidu=weidu/1000000
        jingdu=float(jingdu[:-1])
        jingdu=jingdu/1000000
        day=int(epdate[0:2])
        month=int(epdate[2:4])
        year=int(epdate[4:])
        
        hour=int(eptime[0:2])
        minute=int(eptime[2:4])
        second=int(eptime[4:])
        year += 2000
        now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        t=datetime.datetime(year, month, day, hour, minute, second) + TD_8HOUR
        t=t.strftime("%y-%m-%d %H:%M:%S")
        #print(t)
        #print(epid,eptime,epdate,weidu,bl0,jingdu,direction,speedD,state,userAlarm,bl1,rNum)
        return ('NULL',epid,now,t,jingdu,weidu,direction,speedD,0,state)
