#!/usr/bin/python3
"""Module for adding two integers."""


def add_integer(a, b=98):
    """Add two integers and return the result."""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    # detect infinity without importing modules
    if a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")

    if b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
