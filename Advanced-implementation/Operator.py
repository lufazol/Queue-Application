class Operator:

    def __init__(self, id, state, currentCallId):
        self.id = id
        self.state = state
        self.currentCallId = currentCallId

    def receivesCall(self, callId):
        self.state = "ringing"
        self.currentCallId = callId
        return f"Call {callId} ringing for operator {self.id}"
    
    def answersCall(self):
        self.state = "busy"
        return f"Call {self.currentCallId} answered by operator {self.id}"

    def finishesCall(self):
        self.state = "available"
        finishedCallId = self.currentCallId
        self.currentCallId = "0"
        return f"Call {finishedCallId} finished and operator {self.id} available"

    def rejectsCallAndReturnsCallId(self):
        self.state = "available"
        rejectedCallId = self.currentCallId
        self.currentCallId = "0"
        return rejectedCallId, f"Call {rejectedCallId} rejected by operator {self.id}"
    
    def missesCall(self):
        self.state = "available"
        missedCallId = self.currentCallId
        self.currentCallId = "0"
        return f"Call {missedCallId} missed"

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
