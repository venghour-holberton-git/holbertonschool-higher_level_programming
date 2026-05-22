#!/usr/bin/python3
"""Text indentation module."""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?' and ':'."""

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    n = len(text)

    while i < n:
        print(text[i], end="")

        if text[i] in ".?:":
            print("\n")
            i += 1

            while i < n and text[i] == " ":
                i += 1
            continue

        i += 1

if __name__ == "__main__":
    t = "heellll jenifer jkdsfa? nn baka:nn"
    text_indentation(t)
