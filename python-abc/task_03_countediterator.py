#!/usr/bin/python3

class CountedIterator():
    def __init__(self, items):
        self.__iterator = iter(items)
        self.__count = 0

    def get_count(self):
        return self.__count
    def __next__(self):
        next(self.__iterator)
        self.__count += 1
    def __iter__(self):
        return self

if __name__ == "__main__":
    l1 = CountedIterator([1, 2, 3, 4])
    print(l1.get_count())
    next(l1)
    print(l1.get_count())
    try:
        while True:
            item = next(l1)
            print(f"Got {item}, total {l1.get_count()} items iterated.")
    except StopIteration:
        print("No more items.")
