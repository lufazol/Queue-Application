from twisted.internet import reactor, protocol
import json

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        firstCommand, id = input().split()
        dictWithCommandAndId = {"command": "empty","id": "empty"}
        dictWithCommandAndId["command"] = firstCommand
        dictWithCommandAndId["id"] = id
        jsonCommand = json.dumps(dictWithCommandAndId)
        self.transport.write(jsonCommand.encode('utf-8'))

    def dataReceived(self, data):
        #data = data.decode("utf-8")
        #print("Server said:", data)
        data = data.decode('utf-8')
        messageReceived = json.loads(data)
        for message in messageReceived["message"]:
            print(message)
        firstCommand, id = input().split()
        dictWithCommandAndId = {"command": "empty","id": "empty"}
        dictWithCommandAndId["command"] = firstCommand
        dictWithCommandAndId["id"] = id       
        jsonCommand = json.dumps(dictWithCommandAndId)
        self.transport.write(jsonCommand.encode('utf-8'))
        #self.transport.write(input().encode('utf-8'))
        #self.transport.loseConnection()

class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost.")
        reactor.stop()

reactor.connectTCP("localhost", 5678, EchoFactory())
reactor.run()        