#!/usr/bin/python3
"""class module"""


class Rectangle():
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """assign value to the class"""
        self.width = width
        self.height = height

    def __str__(self):
        print_str = ""
        if self.__width == 0 or self.__height == 0:
            return print_str
        for y in range(self.__height):
            for x in range(self.__width):
                print_str += "#"
            if y != self.__height - 1:
                print_str += "\n"
        return print_str

    @property
    def width(self):
        """getter"""
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

if __name__ == "__main__":
    my_rec = Rectangle(2, 3)
    print(str(my_rec))
    rec2 = Rectangle(0, 5)
    """print(str(rec2))"""
