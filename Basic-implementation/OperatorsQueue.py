class OperatorsQueue:
    
    def __init__(self, queue):
        self.queue = queue

    def receivesOperator(self, operator):
        self.queue.append(operator)

    def hasAvailableOperator(self):
        for operator in self.queue:
            if operator.state == "available":
                return True
    
    def getOperator(self, id):
        for operator in self.queue:
            if operator.id == id:
                return operator
    
    def getOperatorWithCall(self, callId):
        for operator in self.queue:
            if operator.currentCallId == callId:
                return operator