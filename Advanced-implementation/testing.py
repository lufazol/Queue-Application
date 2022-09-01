
def testing(receivedLetter):
    dictTest = {"message": list()}

    if receivedLetter == "a":
        dictTest["message"].append("You typed A")
        dictTest["message"].append("What will you type after A?")
        return dictTest    