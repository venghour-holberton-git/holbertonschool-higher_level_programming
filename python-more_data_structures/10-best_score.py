#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    get_value = lambda item: item[1]
    sorted_score = sorted(a_dictionary.items(), key = get_value)
    new_array = [k for k, v in sorted_score]
    return new_array[-1]
