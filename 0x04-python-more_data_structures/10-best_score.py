#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    mv = 0
    mk = None
    for x, i in a_dictionary.items():
        if i > mv:
            mv = i
            mk = x
    return mk
