from collections import deque
import Operator, OperatorsQueue, CallsQueue
from Command import Command
from auxiliaryFunctions import *

def callCenter(incomingCommand, callsQueue, operatorsQueue):
    '''
    Takes the incoming command from the client, the calls queue
    and the operators queue to process them in the call center
    function.

    Returns a dictionary with the response and updates de calls
    queue and the operators queue.
    '''

    messagesDict = {"response": list()}

    command = Command(incomingCommand["command"])
    id = incomingCommand["id"]

    if command.isCall():
        message = receivesCall(id)
        messagesDict["response"].append(message)
        if operatorsQueue.hasAvailableOperator():
            message = setsCallToAvailableOperator(id, operatorsQueue)
            messagesDict["response"].append(message)
        else:
            message = callsQueue.storesReceivedCall(id)
            messagesDict["response"].append(message)

    elif command.isAnswer():
        operator = isLookedForInOperatorsQueue(id, operatorsQueue)
        message = operator.answersCall()
        messagesDict["response"].append(message)        
    
    elif command.isReject():
        operator = isLookedForInOperatorsQueue(id, operatorsQueue)
        rejectedCallId, message = operator.rejectsCallAndReturnsCallId()
        messagesDict["response"].append(message)
        callsQueue.storesRejectedCall(rejectedCallId)
        if callsQueue.hasCall():
            message = callsQueue.hasCallResolved(operator)
            messagesDict["response"].append(message)        

    elif command.isHangUp():
        if callIsWithAnOperator(operatorsQueue, id):
            operator = operatorsQueue.getOperatorWithCall(id)

            if operator.isBusy():
                message = operator.finishesCall()
                messagesDict["response"].append(message)
                if callsQueue.hasCall(): 
                    message = callsQueue.hasCallResolved(operator)
                    messagesDict["response"].append(message)         

            elif operator.hasRingingCall():
                message = operator.missesCall()
                messagesDict["response"].append(message)
                if callsQueue.hasCall():         
                    message = callsQueue.hasCallResolved(operator)
                    messagesDict["response"].append(message)         
        else:
            message = callsQueue.missesCall(id)
            messagesDict["response"].append(message)         

    return messagesDict, callsQueue, operatorsQueue
