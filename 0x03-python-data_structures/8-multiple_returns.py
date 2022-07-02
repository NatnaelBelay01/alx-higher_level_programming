#!/usr/bin/python3
def multiple_returns(sentence):
    leng = 0
    if sentence:
        for i in sentence:
            leng += 1
        return l, sentence[0]
    else:
        return leng, None
