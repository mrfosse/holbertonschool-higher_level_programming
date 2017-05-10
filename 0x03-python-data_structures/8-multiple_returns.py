#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if l == 0:
        c = None
    else:
        c = sentence[0]
    new = (l, c)
    return new
