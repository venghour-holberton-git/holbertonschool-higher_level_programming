#!/usr/bin/python3
"""square module"""


class Square:
    """Defines a square with size and position, and can compute area or print itself."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square.

        Args:
            size (int): The size of the square (side length). Default is 0.
            position (tuple): A tuple of 2 positive integers representing
                              horizontal and vertical offsets. Default is (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(n, int) for n in value) or
            not all(n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Compute the area of the square.

        Returns:
            int: The area (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character.

        If size is 0, prints an empty line.

        The square is shifted according to position:
        - position[0]: horizontal spaces
        - position[1]: vertical empty lines
        """
        if self.__size == 0:
            print()
            return

        # vertical offset
        for _ in range(self.__position[1]):
            print()

        # square body
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
