#!/usr/bin/python3

def roman_to_int(roman_string):
    i = 0
    total = 0
    temp_value = 0
    for c in roman_string:
        if c == 'I':
            temp_value += 1
            continue
        if c == 'V' and temp_value == 0:
            total += 5
            temp_value = 0
            continue
        if c == 'V' and temp_value != 0:
            total += 4
            temp_value = 0
            continue
        if c == 'X' and temp_value == 0:
            total += 10
            temp_value = 0
            continue
        if c == 'X' and temp_value != 0:
            total += 9
            temp_value = 0
            continue
        if c == 'L':
            total += 50
            temp_value = 0
            continue
        if c == 'C':
            total += 100
            temp_value = 0
            continue
        if c == 'D':
            total += 500
            temp_value = 0
            continue
        if temp_value == 3:
            total += temp_value
    if temp_value != 0:
        total += temp_value
    return total
