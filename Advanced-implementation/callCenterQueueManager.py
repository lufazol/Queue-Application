from twisted.internet import protocol, reactor
import json
from callCenter import callCenter
import Operator, OperatorsQueue, CallsQueue
from auxiliaryFunctions import *

class Server(protocol.Protocol):
	def __init__(self):
		self.callsQueue = createsCallsQueue()
		self.operatorsQueue = createsOperatorsQueue()

		operatorA = createsOperator("A")
		self.operatorsQueue.receivesOperator(operatorA)

		operatorB = createsOperator("B")
		self.operatorsQueue.receivesOperator(operatorB)


	def dataReceived(self, data):

		# decodes the data and make the JSON string into dict
		data = data.decode('utf-8')
		commandReceived = json.loads(data)

		# sends the info to the call center
		response, self.callsQueue, self.operatorsQueue = callCenter(commandReceived, 
		self.callsQueue, self.operatorsQueue)

		# sends the response to the client
		jsonResponse = json.dumps(response)			
		self.transport.write(jsonResponse.encode("utf-8"))
		
		

class ServerFactory(protocol.Factory):
	def buildProtocol(self, addr):
		return Server()


reactor.listenTCP(5678, ServerFactory())
reactor.run()
