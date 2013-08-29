#coding=utf-8
from SuperServerFactory import SuperFactory
from TCPServer.Protocol.TianHeProtocol import TianHeProtocol

class TianHeFactory(SuperFactory):
    factoryKey='TianHe'
    devepid={}
    #记录正在连接的设备数量
    numProtocols=0
    def buildProtocol(self, addr):
        return TianHeProtocol(self)

