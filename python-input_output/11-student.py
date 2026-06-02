#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the instance."""
        if type(attrs) is list:
            result = {}
            for attr in attrs:
                if type(attr) is str and hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes using a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
