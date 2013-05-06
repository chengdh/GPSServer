#coding=utf-8
from SuperServerFactory import SuperFactory
from TCPServer.Protocol.YouWeiProtocol import YouWeiProtocol

class YouWeiFactory(SuperFactory):
    factoryKey='YouWei'
    devepid={}
    #记录正在连接的设备数量
    numProtocols=0
    def buildProtocol(self, addr):
        return YouWeiProtocol(self)

