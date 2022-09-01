from collections import deque
from CallsQueue import CallsQueue
from OperatorsQueue import OperatorsQueue
from Operator import Operator

def createsCallsQueue():
    return CallsQueue(deque())

def createsOperatorsQueue():
    return OperatorsQueue(deque())

def createsOperator(operatorId):
    return Operator(operatorId, "available", "0")

def receivesCall(callId):
    return f"Call {callId} received"

def isLookedForInOperatorsQueue(searchedOperatorId, operatorsQueue):
    for operator in operatorsQueue.queue:
        if operator.id == searchedOperatorId:
            return operator    

def setsCallToAvailableOperator(callId, operatorsQueue):
    for operator in operatorsQueue.queue:
        if operator.state == "available":
            return operator.receivesCall(callId)    

def callIsWithAnOperator(operatorsQueue, callId):
    for operator in operatorsQueue.queue:
        if operator.currentCallId == callId:
            return True
    return False
