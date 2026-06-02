#!/usr/bin/python3
"""wite module"""


def write_file(filename="", text=""):
    """wrtie function"""
    with open(filename, encoding="utf-8") as f:
        f.write(text)
