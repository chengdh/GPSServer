#coding=utf-8
from twisted.internet import protocol

class SuperFactory(protocol.Factory):
    factoryKey='superServer'
    devepid={}
    #记录正在连接的设备数量
    numProtocols=0
    
    def killAllConnection(self):
        print(self.devepid)
        for client in self.devepid:
           self.devepid[client].transport.loseConnection()



