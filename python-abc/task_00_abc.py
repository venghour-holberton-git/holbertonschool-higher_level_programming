#!/usr/bin/python3
from abc import ABC, abstractmethod
"""Animal module"""

class Animal(ABC):
    """Animal abstract class"""

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """Dog class"""

    def sound(self):
        return "Bark"

class Cat(Animal):
    """Cat class"""

    def sound(self):
        return "Meow"
