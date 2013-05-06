#coding=utf-8
import sys
from zope.interface import implements
from twisted.python import usage
from twisted.plugin import IPlugin
from twisted.application.service import IServiceMaker
from twisted.application import internet
#from TCPServer.Factory import *
from TCPServer.Factory import simple_factory,TianHeServerFactory
#加入etc/目录
sys.path.append("etc")
import config as global_config



class Options(usage.Options):
    optParameters = [
        ["port", "p", 5000, "TCP Server 监听端口."],
        ["factory_key","fk","simple_factory","默认的factory_key"]
        ]


class GPSServiceMaker(object):
    implements(IServiceMaker, IPlugin)
    options = Options
    tapname = "gps_server"
    description = "%s协议服务." % tapname
 
    def makeService(self, options):
        """
        Construct a TCPServer from a factory defined in myproject.
        """

        factory_key = options['factory_key']
        factory_object = eval(global_config.dic[options['factory_key']]['factory'])
        factory_object.factoryKey = factory_key
        return internet.TCPServer(int(options['port']),factory_object)

# Now construct an object which *provides* the relevant interfaces
# The name of this variable is irrelevant, as long as there is *some*
# name bound to a provider of IPlugin and IServiceMaker.

serviceMaker = GPSServiceMaker()
