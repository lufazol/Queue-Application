from collections import deque


class OperatorsQueue:
    
    def __init__(self, queue):
        self.queue = queue

    def addOperator(self, operator):
        self.queue.appendleft(operator)

    def hasAvailableOperator(self):
        for operator in self.queue:
            if operator.state == "available":
                return True
    
    def setCallToAvailableOperator(self, callId):
        for operator in self.queue:
            if operator.state == "available":
                operator.receivesCall(callId)
    
    def getOperatorWithRingingCall(self, callId):
        for operator in self.queue:
            if operator.state == "ringing" and operator.currentCallId == callId:
                return operator

    

class Operator:

    def __init__(self, id, state, currentCallId):
        self.id = id
        self.state = state
        self.currentCallId = currentCallId

    def receivesCall(self, callId):
        self.state = 'ringing'
        self.currentCallId = callId
        print(f"Call {callId} ringing for operator {self.id}")
    
    def answersCall(self):
        self.state = 'busy'
        print(f"Call {self.currentCallId} answered by operator {self.id}")

    def finishesCall(self):
        self.state = 'available'
        print(f"Call {self.currentCallId} finished and operator {self.id} available" )
        self.currentCallId = '0'

    def rejectsCall(self):
        self.state = 'available'
        print(f"Call {self.currentCallId} rejected by operator {self.id}")
        self.currentCallId = '0'



class CallsQueue:

    def __init__(self, queue):
        self.queue = queue

    '''
    def putInCallsQueue(self, callId):
        self.queue.appendleft(callId)
        print(f"Call {callId} waiting in queue")
    '''
    
    def hasCallInQueue(self):
        return self.queue
    
    def isHungUp(self):
        pass

def putCallInCallsQueue(callId, callsQueue):
    callsQueue.appendleft(callId)
    print(f"Call {callId} waiting in queue")


def main():

    callsQueue = CallsQueue(deque())
    operatorsQueue = OperatorsQueue(deque())
    operatorA = Operator("A", "available", "0")
    operatorB = Operator("B", "available", "0")



    receivedCommand, callId = input().split()

    if receivedCommand == "call":
        print(f"Call {callId} received")
        if operatorsQueue.hasAvailableOperator():
            #actually make into stand-alone function
            operatorsQueue.setCallToAvailableOperator(callId)
        else:
            putCallInCallsQueue(callId, callsQueue)
    elif receivedCommand == "answer":
        operator = operatorsQueue.getOperatorWithRingingCall(callId)
        operator.answersCall()
    
