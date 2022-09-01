from twisted.internet import reactor, protocol
import json

class Client(protocol.Protocol):
    def connectionMade(self):

        # gets the first input
        dictWithCommandAndId = takeInput()

        # converts the dict to a JSON string, encodes it and sends
        # to server
        jsonCommand = json.dumps(dictWithCommandAndId)
        self.transport.write(jsonCommand.encode('utf-8'))

    def dataReceived(self, data):

        # decodes the data received, converts the JSON string
        # to dict and print each message in the "response" key
        data = data.decode('utf-8')
        messageReceived = json.loads(data)
        for message in messageReceived["response"]:
            print(message)

        # takes input again
        dictWithCommandAndId = takeInput()
       
       # converts the dict to a JSON string and sends it to server
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

def takeInput():
    
    # gets the first input
    firstCommand, id = input().split()

    # creates a dict and assign the values for each key
    dictWithCommandAndId = {"command": "empty","id": "empty"}
    dictWithCommandAndId["command"] = firstCommand
    dictWithCommandAndId["id"] = id

    return dictWithCommandAndId


reactor.connectTCP("localhost", 5678, ClientFactory())
reactor.run()        