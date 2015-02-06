from twisted import reactor,protocol

class Echo(protocol.Protocol):
    def dataReceived(self,data):
        self.transport.write("Hello,Dacy...")

class EchoFactory(protocol.Factory):
    def buildProtocol(self,addr):
        return Echo()