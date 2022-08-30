from collections import deque


class OperatorsQueue:
    
    def __init__(self, queue):
        self.queue = queue

    def hasAvailableOperator(self):
        pass   
    

class Operator:

    def __init__(self, id, state, currentCallId):
        self.id = id
        self.state = state
        self.currentCallId = currentCallId

    def receivesCall(self, callId):
        self.state = 'ringing'
        self.currentCallId = callId
    
    def answersCall(self):
        self.state = 'busy'

    def finishesCall(self):
        self.state = 'available'
        self.currentCallId = '0'

    def rejectsCall(self):
        self.state = 'available'
        self.currentCallId = '0'


class CallsQueue:

    def __init__(self, queue):
        pass




def createOperatorsQueue():
    operatorsQueue = deque()
    return operatorsQueue
 
