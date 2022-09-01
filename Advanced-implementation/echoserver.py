from twisted.internet import protocol, reactor
import json
from callCenter import callCenter

class Echo(protocol.Protocol):
	def dataReceived(self, data):
		data = data.decode('utf-8')
		commandReceived = json.loads(data)
		#self.transport.write(data)

		dictTest = callCenter(commandReceived["command"], commandReceived["id"])
		jsonDictTest = json.dumps(dictTest)			
		self.transport.write(jsonDictTest.encode("utf-8"))
		
		

class EchoFactory(protocol.Factory):
	def buildProtocol(self, addr):
		return Echo()


reactor.listenTCP(5678, EchoFactory())
reactor.run()
