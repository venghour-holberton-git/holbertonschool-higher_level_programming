#!/usr/bin/python3

def getPreferStudents(students = []):
    new_list = list(filter(lambda x: x[1] > 25, students))
    new_list.sort(key = lambda student: student[0])
    filter_list = tuple([student[0] for student in new_list])
    return filter_list

students = [
    ('Same', 24),
    ('Zac', 24),
    ('Sean', 23),
    ('Venghour', 28),
    ('Lachlan', 28)
        ]

print(getPreferStudents(students))
