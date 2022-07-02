#!/usr/bin/python3
def multiple_returns(sentence):
    l = 0
    if sentence:
        for i in sentence:
            l += 1
        return l, sentence[0]
    else:
        return l, None
