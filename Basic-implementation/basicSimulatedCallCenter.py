from collections import deque

class OperatorsQueue:
    
    def __init__(self, queue):
        self.queue = queue

    def receivesOperator(self, operator):
        self.queue.append(operator)

    def hasAvailableOperator(self):
        for operator in self.queue:
            if operator.state == "available":
                return True
    
    def setCallToAvailableOperator(self, callId):
        for operator in self.queue:
            if operator.state == "available":
                operator.receivesCall(callId)
                break
    
    def getOperator(self, id):
        for operator in self.queue:
            if operator.id == id:
                return operator
    
    def getOperatorWithCall(self, callId):
        for operator in self.queue:
            if operator.currentCallId == callId:
                return operator

    

class Operator:

    def __init__(self, id, state, currentCallId):
        self.id = id
        self.state = state
        self.currentCallId = currentCallId

    def receivesCall(self, callId):
        self.state = "ringing"
        self.currentCallId = callId
        print(f"Call {callId} ringing for operator {self.id}")
    
    def answersCall(self):
        self.state = "busy"
        print(f"Call {self.currentCallId} answered by operator {self.id}")

    def finishesCall(self):
        self.state = "available"
        print(f"Call {self.currentCallId} finished and operator {self.id} available" )
        self.currentCallId = "0"

    def rejectsCall(self):
        self.state = "available"
        print(f"Call {self.currentCallId} rejected by operator {self.id}")
        rejectedCallId = self.currentCallId
        self.currentCallId = "0"
        return rejectedCallId
    
    def missesCall(self):
        self.state = "available"
        print(f"Call {self.currentCallId} missed")
        self.currentCallId = "0"



class CallsQueue:

    def __init__(self, queue):
        self.queue = queue

    def hasCall(self):
        return self.queue
    
    def getsNewCall(self, callId):
        self.queue.append(callId)
        print(f"Call {callId} waiting in queue")

    def hasCallResolved(self, operator):
        if self.hasCall():
            callId = self.queue[0]
            operator.receivesCall(callId)
            self.hasCallRemoved()        

    def hasCallRemoved(self):
        self.queue.popleft()
    
    def missesCall(self, callId):
        for call in self.queue:
            if call == callId:
                print(f"Call {callId} missed")
                self.queue.remove(call)



def operatorHasCallId(operatorsQueue, callId):
    for operator in operatorsQueue.queue:
        if operator.currentCallId == callId:
            return True
    return False



def main():

    callsQueue = CallsQueue(deque())
    operatorsQueue = OperatorsQueue(deque())
    operatorA = Operator("A", "available", "0")
    operatorB = Operator("B", "available", "0")
    operatorsQueue.receivesOperator(operatorA)
    operatorsQueue.receivesOperator(operatorB)

    while True:
        receivedCommand, id = input().split()

        if receivedCommand == "call":
            print(f"Call {id} received")
            if operatorsQueue.hasAvailableOperator():
                #actually make into stand-alone function
                operatorsQueue.setCallToAvailableOperator(id)
            else:
                callsQueue.getsNewCall(id)

        elif receivedCommand == "answer":
            operator = operatorsQueue.getOperator(id)
            operator.answersCall()
        
        elif receivedCommand == "reject":
            operator = operatorsQueue.getOperator(id)
            rejectedCallId = operator.rejectsCall()
            callsQueue.getsNewCall(rejectedCallId)
            callsQueue.hasCallResolved(operator)

        elif receivedCommand == "hangup":
            if operatorHasCallId(operatorsQueue, id):
                operator = operatorsQueue.getOperatorWithCall(id)
                if operator.state == "busy":
                    operator.finishesCall()
                    callsQueue.hasCallResolved(operator)
                elif operator.state == "ringing":
                    operator.missesCall()
                    callsQueue.hasCallResolved(operator)
            else:
                callsQueue.missesCall(id)

main()

