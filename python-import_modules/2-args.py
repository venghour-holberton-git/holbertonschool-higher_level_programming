#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg_length = len(sys.argv) - 1
    s_text = '' if arg_length == 1 else 's'
    extra_text = ':' if len(sys.argv) - 1 != 0 else '.'
    print(f"{arg_length} argument{s_text}{extra_text}")
    if len(sys.argv) - 1 != 0:
        index = 1
        for s in sys.argv[1:]:
            if index != 0:
                print(f"{index}: {s}")
            index += 1
