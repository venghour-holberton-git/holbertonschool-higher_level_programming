#!/usr/bin/python3

class CountedIterator():
    def __init__(self, items):
        self.__iterator = iter(items)
        self.__count = 0

    def get_count(self):
        return self.__count
    def __next__(self):
        self.__count += 1
        return next(self.__iterator)

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
