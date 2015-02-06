from twisted.internet import reactor,protocol

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("Hello,Dacy!")

    def connectionLost(self,reason):
        print("CONNECTION LOST!")

    def dataReceived(self,data):
        print("SERVER SEND %s"%data)
        self.transport.loseConnection()

class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self,addr):
        return EchoClient()

    def clientConnectionLost(self,connector,reason):
        print("CONNECTION LOST FACTORY!")
        reactor.stop()

    def clientConnectionFiled():
        print("CONNECTION FILED!")
        reactor.stop()

reactor.connectTCP("localhost",8800,EchoFactory())
reactor.run()