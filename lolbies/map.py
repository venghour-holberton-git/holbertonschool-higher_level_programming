#!/usr/bin/python3

class Map():
    __ALLOWED_TEAMS = ("blue", "red")
    __COUNT = 0
    
    def __init__(self, name, blue=None, red=None):
        if Map.__COUNT >= 1:
            raise ValueError("can't have more than one map")
        Map.__COUNT += 1
        self.name = name
        if blue is not None:
            self.blue = blue
        if red is not None:
            self.red = red
        print(f"Welcome to {name}")

    def __del__(self):
        Map.__COUNT = 0

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def red(self):
        return self.__red

    @red.setter
    def red(self, value):
        if not isinstance(value, list):
            raise TypeError("must be a list")
        if len(value) == 5:
            raise ValueError("must be a 5 player in the team")
        self.__red = value

    @property
    def blue(self):
        return self.__blue

    @blue.setter
    def blue(self, value):
        if not isinstance(value, list):
            raise TypeError("must be a list")
        if len(value) == 5:
            raise ValueError("must be a 5 player in the team")
        self.__blue = value

    def add_summoner(self, summoner, team):
        if team not in Map.__ALLOWED_TEAM:
            raise TypeError("Team type is not allowed")
        if team is "red":
            self.__red.append(summoner)
            if len(self.__red) > 5:
                raise ValueError("Too many players in red team")
        if team is "blue":
            self.__blue.append(summoner)
            if len(self.__blue) > 5:
                raise ValueError("Too many player in blue team")

