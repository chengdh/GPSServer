#coding=utf-8
from zope.interface import implements

from twisted.python import usage
from twisted.plugin import IPlugin
from twisted.application.service import IServiceMaker
from twisted.application import internet

from TCPServer.Factory.simple_factory import  SimpleFactory 


class Options(usage.Options):
    optParameters = [["port", "p", 5010, "The port number to listen on."]]


class MyServiceMaker(object):
    implements(IServiceMaker, IPlugin)
    tapname = "myproject"
    description = "Run this! It'll make your dog happy."
    options = Options

    def makeService(self, options):
        """
        Construct a TCPServer from a factory defined in myproject.
        """
        return internet.TCPServer(5010, SimpleFactory())


# Now construct an object which *provides* the relevant interfaces
# The name of this variable is irrelevant, as long as there is *some*
# name bound to a provider of IPlugin and IServiceMaker.

serviceMaker = MyServiceMaker()
