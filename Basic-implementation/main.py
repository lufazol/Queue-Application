from collections import deque
import Operator, OperatorsQueue, CallsQueue
from Command import Command
from auxiliaryFunctions import *

def main():

    callsQueue = createsCallsQueue()
    operatorsQueue = createsOperatorsQueue()

    operatorA = createsOperator("A")
    operatorsQueue.receivesOperator(operatorA)

    operatorB = createsOperator("B")
    operatorsQueue.receivesOperator(operatorB)

    while True:
        receivedCommand, id = input().split()
        command = Command(receivedCommand)

        if command.isCall():
            receivesCall(id)
            if operatorsQueue.hasAvailableOperator():
                setsCallToAvailableOperator(id, operatorsQueue)
            else:
                callsQueue.storesReceivedCall(id)

        elif command.isAnswer():
            operator = isLookedForInOperatorsQueue(id, operatorsQueue)
            operator.answersCall()
        
        elif command.isReject():
            operator = isLookedForInOperatorsQueue(id, operatorsQueue)
            rejectedCallId = operator.rejectsCallAndReturnsCallId()
            callsQueue.storesRejectedCall(rejectedCallId)
            callsQueue.hasCallResolved(operator)

        elif command.isHangUp():
            if callIsWithAnOperator(operatorsQueue, id):
                operator = operatorsQueue.getOperatorWithCall(id)

                if operator.isBusy():
                    operator.finishesCall()
                    callsQueue.hasCallResolved(operator)

                elif operator.hasRingingCall():
                    operator.missesCall()
                    callsQueue.hasCallResolved(operator)
            else:
                callsQueue.missesCall(id)

main()

