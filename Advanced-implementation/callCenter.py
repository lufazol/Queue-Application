from collections import deque
import Operator, OperatorsQueue, CallsQueue
from Command import Command
from auxiliaryFunctions import *

def callCenter(receivedCommand, id):

    messagesDict = {"messages": list()}

    callsQueue = createsCallsQueue()
    operatorsQueue = createsOperatorsQueue()

    operatorA = createsOperator("A")
    operatorsQueue.receivesOperator(operatorA)

    operatorB = createsOperator("B")
    operatorsQueue.receivesOperator(operatorB)

    command = Command(receivedCommand)

    if command.isCall():
        message = receivesCall(id)
        messagesDict["messages"].append(message)
        if operatorsQueue.hasAvailableOperator():
            message = setsCallToAvailableOperator(id, operatorsQueue)
            messagesDict["messages"].append(message)
        else:
            message = callsQueue.storesReceivedCall(id)
            messagesDict["messages"].append(message)

    elif command.isAnswer():
        operator = isLookedForInOperatorsQueue(id, operatorsQueue)
        message = operator.answersCall()
        messagesDict["messages"].append(message)        
    
    elif command.isReject():
        operator = isLookedForInOperatorsQueue(id, operatorsQueue)
        rejectedCallId, message = operator.rejectsCallAndReturnsCallId()
        messagesDict["messages"].append(message)
        callsQueue.storesRejectedCall(rejectedCallId)
        message = callsQueue.hasCallResolved(operator)
        messagesDict["messages"].append(message)        

    elif command.isHangUp():
        if callIsWithAnOperator(operatorsQueue, id):
            operator = operatorsQueue.getOperatorWithCall(id)

            if operator.isBusy():
                message = operator.finishesCall()
                messagesDict["messages"].append(message) 
                message = callsQueue.hasCallResolved(operator)
                messagesDict["messages"].append(message)         

            elif operator.hasRingingCall():
                message = operator.missesCall()
                messagesDict["messages"].append(message)         
                message = callsQueue.hasCallResolved(operator)
                messagesDict["messages"].append(message)         
        else:
            message = callsQueue.missesCall(id)
            messagesDict["messages"].append(message)         

    return messagesDict
