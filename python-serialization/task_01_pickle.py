#!/usr/bin/python3
"""Module for serializing and deserializing a custom object."""

import pickle


class CustomObject:
    """A custom object with serialization support."""

    def __init__(self, name, age, is_student):
        """Initialize the object."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object and save it to a file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an object from a pickle file."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError, EOFError):
            return None
