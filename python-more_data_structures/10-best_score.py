#!/usr/bin/python3

def get_value(item):
    return item[1]
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    sorted_score = sorted(a_dictionary.items(), key = get_value)
    new_array = [k for k, v in sorted_score]
    return new_array[-1]
