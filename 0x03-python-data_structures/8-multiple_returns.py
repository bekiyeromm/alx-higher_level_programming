#!usr/bin/python3
def multiple_returns(sentence):
    first = ()
    if len(sentence) == 0:
        first = "None"
        length = 0
    else:
        first = sentence[0]
        length = len(sentence)
    return (length, first)
