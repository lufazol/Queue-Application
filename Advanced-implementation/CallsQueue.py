
class CallsQueue:

    def __init__(self, queue):
        self.queue = queue

    def hasCall(self):
        return self.queue
    
    def storesReceivedCall(self, callId):
        self.queue.append(callId)
        return f"Call {callId} waiting in queue"

    def hasCallResolved(self, operator):
        callId = self.queue[0]
        self.hasCallRemoved()  
        return operator.receivesCall(callId)

    def hasCallRemoved(self):
        self.queue.popleft()
    
    def missesCall(self, callId):
        for call in self.queue:
            if call == callId:
                self.queue.remove(call)
                return f"Call {callId} missed"

    def storesRejectedCall(self, callId):
        self.queue.append(callId)