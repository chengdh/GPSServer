#coding=utf-8
from zope.interface import implements

from twisted.python import usage
from twisted.plugin import IPlugin
from twisted.application.service import IServiceMaker
from twisted.application import internet
from TCPServer import config as global_config


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

        return internet.TCPServer(int(options['port']), global_config.dic[options['factory_key']]['factory'])

# Now construct an object which *provides* the relevant interfaces
# The name of this variable is irrelevant, as long as there is *some*
# name bound to a provider of IPlugin and IServiceMaker.

serviceMaker = GPSServiceMaker()