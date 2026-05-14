#!/usr/bin/python3

def best_score(a_dictionary):
    sorted_score = [k for k, v in sorted(a_dictionary.items(), key = lambda item: item[1])]
    return sorted_score[-1]
