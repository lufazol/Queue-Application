class Command:

    def __init__(self, receivedCommand):
        self.receivedCommand = receivedCommand

    def isCall(self):
        if self.receivedCommand == "call":
            return True
        else:
            return False
    
    def isAnswer(self):
        if self.receivedCommand == "answer":
            return True
        else:
            return False

    def isReject(self):
        if self.receivedCommand == "reject":
            return True
        else:
            return False
    
    def isHangUp(self):
        if self.receivedCommand == "hangup":
            return True
        else:
            return False
