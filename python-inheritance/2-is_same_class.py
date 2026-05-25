#!/usr/bin/python3
"""function module"""

MyList = __import__("1-my_list").MyList

def is_same_class(obj, a_class):
    """return if same as class"""
    return type(obj) is a_class
