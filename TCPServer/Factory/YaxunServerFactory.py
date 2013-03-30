#coding=utf-8
from SuperServerFactory import SuperFactory
from Protocol.YaxunProtocol import YaxunProtocol

class YaxunFactory(SuperFactory):
    factoryKey='Yaxun'
    devepid={}
    #记录正在连接的设备数量
    numProtocols=0
    def buildProtocol(self, addr):
        return YaxunProtocol(self)

