__author__ = 'luozi'
from twisted.internet import reactor,protocol

class QuickconnectedProtocol(protocol.Protocol):
    def connectionMade(self):
        print ("Connected to %s" % self.transport.getPeer().host)
        self.transport.loseConnection()
class BasicCilentFactory(protocol.ClientFactory):
    protocol =QuickconnectedProtocol

    def clientConnectionLost(self, connector, reason):
        print('Lost connection :%s'% reason.getErrorMessage())
        reactor.stop()
    def clientConnectionFailed(self, connector, reason):
        print('Connection failed: %s'%reason.getErrorMessage())
        reactor.stop()

reactor.connectTCP('www.google.com',80,BasicCilentFactory())
reactor.run()