#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    c = sentence[0]
    if l < 1:
        new = (0, )
        return (new)
    else:
        c = sentence[0]
        new = (l, c)
        return (new)
