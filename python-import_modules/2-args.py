#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    print(f"{len(sys.argv) - 1} arguments{':' if len(sys.argv) - 1 != 0 else '.'}")
    if len(sys.argv) - 1 != 0:
        index = 1
        for s in sys.argv[1:]:
            if index != 0:
                print(f"{index}: {s}")
            index += 1
