#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    c = sentence[0]
    if l == 0:
        c = None
    new = (l, c)
    return new
