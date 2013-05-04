# encoding:utf-8
from twisted.internet import protocol
from twisted.python import log

class SimpleProtocol(protocol.Protocol):

    def __init__(self, factory):
        self.factory = factory
    
    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols+1
        log.msg("connection made: current count = %s" % self.factory.numProtocols)
        connected=True
    
    def dataReceived(self, data):
        log.msg("data receive = %s" % data)
    
    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols-1
        log.msg("connection lost: current count = %s" % self.factory.numProtocols)
