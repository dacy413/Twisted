from twisted.internet import protocol,reactor

class Echo(protocol.Protocol):
    def dataReceived(self,data):
        print("CLIENT is %s DATA IS %s"%(self.transport.client,data))
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self,addr):
        return Echo()

# import pdb;pdb.set_trace()
reactor.listenTCP(8800,EchoFactory())
reactor.run()