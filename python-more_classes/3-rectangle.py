#!/usr/bin/python3
"""class module"""


class Rectangle():
    """Rectangle class"""
    def __init__(self, width, height):
        """assign value to the class"""
        self.width = width
        self.height = height
    def __str__(self):
        print_str = ""
        for y in range(self.__height):
            for x in range(self.__width):
                    print_str += "#"
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
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value
    def area():
        """return the area of the rectangle"""
        return width * height
    def perimeter(self):
        """return rectangle perimeter"""
        return 2 * (width + height)

if __name__ == "__main__":
    my_rec = Rectangle(2, 3)
    print(str(my_rec))
