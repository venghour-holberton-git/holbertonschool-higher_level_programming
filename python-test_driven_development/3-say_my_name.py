#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    full_name = first_name + " " + last_name
    print("My name is {}".format(full_name))

if __name__ == "__main__":
    say_my_name("ooop", "ooii")
