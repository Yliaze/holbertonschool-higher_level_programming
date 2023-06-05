#!/usr/bin/python3
def multiple_returns(sentence):

    if sentence == "":
        return None, None

    first = sentence[0]
    lenght = len(sentence)
    return lenght, first
