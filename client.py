from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver


class ChatClient(LineReceiver):
    def __init__(self, name):
        self.name = name
        self.state = "OFFLINE"
        self.work = True

    def connectionMade(self):
        #while self.work:
            #if self.factory.message is not None:
                #self.sendline(self.factory.message.encode("utf-8"))
                #self.factory.message = None
        pass

    def lineReceived(self, line):
        if self.state == "ONLINE":
            print(line.decode("utf-8"))
        elif self.state == "OFFLINE":
            print(line.decode("utf-8"))
            self.sendLine("{}".format(self.name).encode("utf-8"))
            self.state = "ONLINE"

    def connectionLost(self, reason):
        print("Lost")

    def send_message(self, massage):
        self.sendLine("{}".format(message).encode("utf-8"))

class ChatClientFactory(ClientFactory):
    def __init__(self, name):
        self.name = name

    def clientConnectionFailed(self, connector, reason):
        print("Failed")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Closed")
        reactor.stop()

    def buildProtocol(self, addr):
        self.connection = ChatClient(self.name)
        return self.connection

    def send(self, message):
        self.connection.send_message(massage)

if __name__ == "__main__":

    #argument parser
    import time

    chat = ChatClientFactory("Slava")
    reactor.connectTCP("192.168.4.123", 5000, chat)
    reactor.run()
    while True:
