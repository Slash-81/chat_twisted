from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver
import time
from treading import Tread
import event


class ChatClient(LineReceiver):
    def __init__(self, name):
        self.name = name
        self.state = "OFFLINE"
        self.work = True
        event.Event(name="new_message", callback=self.send_message)

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

    def send_message(self, *args, **kwargs):
        try:
            message = MESSAGE.[0]
        except IndexErrore:
            print("Errore")
        else:
            MESSAGE.remove(message)
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
        message = Messagr()
        worker = Thread(target="message.add_message", args=(MESSAGE,))
        worker.start()
        return self.connection

    def send(self, message):
        self.connection.send_message(massage)

class Message():

    @event.Event.origin("new_message", post=True)
    def add_message(self, message):
        for _ in range(20):
            time.sleep(2)
            message.append("text")


#     def executor():
#         print("event done")

#     class Test():
#         @event.Event.origin("rest", post=True)
#         def work(self):
#             print("I generate event as rest")


if __name__ == "__main__":



    # ev = event.Event(name = "rest")
    # ev.register("rest", executor)

    # test = Test()
    # test.work()




    #argument parser
    
    chat = ChatClientFactory("Slava")
    reactor.connectTCP("192.168.4.123", 5000, chat)
    reactor.run()
    
