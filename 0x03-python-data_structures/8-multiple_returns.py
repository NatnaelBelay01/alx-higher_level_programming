#!/usr/bin/python3
def multiple_returns(sentence):
    leng = 0
    if sentence:
        for i in sentence:
            leng += 1
        return leng, sentence[0]
    else:
        return leng, None
