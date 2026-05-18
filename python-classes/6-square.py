#!/usr/bin/python3
"""square class module"""


class Square:
    """square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not (len(value) == 2 and
                isinstance(value[0], int) and
                isinstance(value[1], int) and
                value[0] >= 0 and
                value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

   def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using #."""

        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print("#" * self.__size) 
