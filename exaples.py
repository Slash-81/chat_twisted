from twisted.internet.protocol import Protocol, ServerFactory
from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ServerEndpoint
import random
import requests

HEADER = "HTTP/1.1 200 OK\r\nDate: Mon, 1 Apr 2019 01:01:01 GMT\r\nContent Type: text/plain\r\nContent Length: 25\r\n\r\n"
URLS = [
"https://habr.com/ru/hub/twisted/",
"https://www.twistedmatrix.com/trac/",
"https://docs.python.org/3/library/select.html"
]

class Echo(Protocol):
    def __init__(self):
        super().__init__()
        data = requests.get(URLS[random.randint(0, 2)])
        lines = []
        for key, value in data.headers.items():
            lines.append(f"{key} {value}")
        header = "\r\n".join(lines + ["\r\n\r\n"])
        html = data.text
        self.respose = f"{header}{html}".encode("utf-8")

    def dataReceived(self, data):
        self.transport.write(self.respose)
        self.transport.loseConnection()

class SrvFactory(ServerFactory):
    def __init__(self, file_name):
        self.file = file_name

    #protocol = Echo
    def buildProtocol(self, addr):
        self.fd.write("{}\n".format(addr))
        return Echo()

    def startFactory(self):
        print("Start!")
        self.fd = open(self.file, 'a')

    def stopFactory(self):
        print("Stop!")
        self.fd.close()


if __name__ == "__main__":
    #factory = SrvFactory()
    #reactor.listenTCP(5000, factory)
    #reactor.run()
    endPoint = TCP4ServerEndpoint(reactor, 5000)
    endPoint.listen(SrvFactory("server.log"))
    reactor.run()
