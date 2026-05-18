#!/usr/bin/python3
"""square module"""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize square with size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

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
