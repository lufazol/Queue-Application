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

    def rejectsCallAndReturnsCallId(self):
        self.state = "available"
        print(f"Call {self.currentCallId} rejected by operator {self.id}")
        rejectedCallId = self.currentCallId
        self.currentCallId = "0"
        return rejectedCallId
    
    def missesCall(self):
        self.state = "available"
        print(f"Call {self.currentCallId} missed")
        self.currentCallId = "0"

    def isBusy(self):
        if self.state == "busy":
            return True
        else:
            return False

    def hasRingingCall(self):
        if self.state == "ringing":
            return True
        else:
            return False
