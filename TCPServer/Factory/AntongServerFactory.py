#coding=utf-8
from SuperServerFactory import SuperFactory
from TCPServer.Protocol.AntongProtocol import AntongProtocol

class AntongFactory(SuperFactory):
    factoryKey='Antong'
    devepid={}
    #记录正在连接的设备数量
    numProtocols=0
    def buildProtocol(self, addr):
        return AntongProtocol(self)
