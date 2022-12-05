#!usr/bin/python3
def multiple_returns(sentence):
    first = ()
    if len(sentence) == 0:
        first = 0, "None"
    else:
        first = len(sentence), sentence[0]
    return (first)
