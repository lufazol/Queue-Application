
class CallsQueue:

    def __init__(self, queue):
        self.queue = queue

    def hasCall(self):
        return self.queue
    
    def storesReceivedCall(self, callId):
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
                break

    def storesRejectedCall(self, callId):
        self.queue.append(callId)