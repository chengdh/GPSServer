#coding=utf-8
from SuperServerFactory import SuperFactory
from TCPServer.Protocol.simple_protocol import SimpleProtocol

class SimpleFactory(SuperFactory):
    factoryKey='simple_test'
    devepid={}
    #记录正在连接的设备数量
    numProtocols=0
    def buildProtocol(self, addr):
        return SimpleProtocol(self)



