#!/usr/bin/python3
"""square module"""

class Square:
    """square class"""
    def __init__(self, size=0):
        self.__size = size
    def size(self):
        return self.__size
    def size(self, value):
        self.__size = value
