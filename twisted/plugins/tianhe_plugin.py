#coding=utf-8
from zope.interface import implements

from twisted.python import usage
from twisted.plugin import IPlugin
from twisted.application.service import IServiceMaker
from twisted.application import internet

from TCPServer.Factory.TianHeServerFactory import  TianHeFactory 
import TCPServer.SqlOpration.SqlOprate  as SqlOprate
import TCPServer.config as global_config


class Options(usage.Options):
    optParameters = [["port", "p", 5000, "The port number to listen on."]]


class MyServiceMaker(object):
    implements(IServiceMaker, IPlugin)
    tapname = "tianhe"
    description = "天河协议服务."
    options = Options

    def makeService(self, options):
        """
        Construct a TCPServer from a factory defined in myproject.
        """
        self.connect_db('TianHe')
        return internet.TCPServer(5000, TianHeFactory())

    def connect_db(self,factory_key):
      '''
      连接数据库
      '''
      db_connect_dic = global_config.dic[factory_key]
      SqlOprate.sqlUnpnConnect(factory_key,db_connect_dic)
      SqlOprate.sqlUnpnhisConnect(factory_key,db_connect_dic)
 


# Now construct an object which *provides* the relevant interfaces
# The name of this variable is irrelevant, as long as there is *some*
# name bound to a provider of IPlugin and IServiceMaker.

serviceMaker = MyServiceMaker()
