#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for option in sorted(dir(hidden_4)):
        if not option.startswith("__"):
            print(option)
