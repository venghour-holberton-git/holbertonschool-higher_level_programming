#!/usr/bin/python3

def roman_to_int(roman_string):
    i = 0
    total = 0
    temp_value = 0
    last_char = ''

    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    for c in roman_string:
        if c == 'I':
            if last_char == 'X':
                total += temp_value
                temp_value = 0
            temp_value += 1
            if temp_value == 3:
                total += temp_value
                temp_value = 0
            last_char = 'I'
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
            temp_value = 10
            if last_char == 'X':
                total += temp_value
                temp_value = 0
            last_char = 'X'
            continue
        if c == 'X' and temp_value != 0:
            if last_char == 'X':
                if temp_value == 9:
                    total += temp_value
                    temp_value = 0
                else:
                    temp_value += 10
                    total += temp_value
                    temp_value = 0
                continue
            temp_value = 9
            continue
        if c == 'L':
            add_value = 50
            if last_char == 'X':
                add_value -= 10
                last_char = 'L'
            total += add_value
            temp_value = 0
            continue
        if c == 'C':
            add_value = 100
            if last_char == 'X':
                add_value -= 10
                last_char = 'C'
            total += add_value
            temp_value = 0
            continue
        if c == 'D':
            add_value = 500
            if last_char == 'C':
                add_value -= 100
                last_char = 'D'
            total += add_value
            temp_value = 0
            continue
    if temp_value != 0:
        total += temp_value
    return total
