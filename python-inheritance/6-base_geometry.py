#!/usr/bin/python3
"""base class module"""


class BaseGeometry:
    """base geometry"""
    def area(self):
        raise Exception("area() is not implemented")
