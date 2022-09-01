from twisted.internet import reactor, protocol
import json

class Client(protocol.Protocol):
    def connectionMade(self):
        firstCommand, id = input().split()
        dictWithCommandAndId = {"command": "empty","id": "empty"}
        dictWithCommandAndId["command"] = firstCommand
        dictWithCommandAndId["id"] = id
        jsonCommand = json.dumps(dictWithCommandAndId)
        self.transport.write(jsonCommand.encode('utf-8'))

    def dataReceived(self, data):
        data = data.decode('utf-8')
        messageReceived = json.loads(data)
        for message in messageReceived["response"]:
            print(message)
        firstCommand, id = input().split()
        dictWithCommandAndId = {"command": "empty","id": "empty"}
        dictWithCommandAndId["command"] = firstCommand
        dictWithCommandAndId["id"] = id       
        jsonCommand = json.dumps(dictWithCommandAndId)
        self.transport.write(jsonCommand.encode('utf-8'))

class ClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return Client()

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost.")
        reactor.stop()

reactor.connectTCP("localhost", 5678, ClientFactory())
reactor.run()        