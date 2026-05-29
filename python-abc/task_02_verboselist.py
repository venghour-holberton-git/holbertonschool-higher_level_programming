#!/usr/bin/python3
"""List module"""


class VerboseList(list):
    """VerboseList class"""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.") 

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index = None):
        popIndex = index if index != None else len(self) - 1
        print(f"Popped [item] from the list.")
        super().pop(popIndex)

if __name__ == "__main__":
    list_2 = VerboseList()
    list_2.append("bnn")
    list_2.extend(["vv", "dffdd"])
    print(list_2)
    list_2.remove('vv')
    print(list_2)
