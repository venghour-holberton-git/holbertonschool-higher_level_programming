#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "and is greater than 5"
if number % 10 > 5:
    str = "and is greater than 5"
elif number % 10 == 0:
    str = "and is 0"
elif number < 6 and number != 0:
    str = "and is less than 6 and not 0"
else:
    str = "don't know"
print(f"{(number % 10)} {str}")
