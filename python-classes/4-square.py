#!/usr/bin/python3
"""square module"""

class Square:
    """square class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        self.__size = value

    def area(self):
        """return square area"""
        return size ** 2
