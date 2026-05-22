#!/usr/bin/python3

from summoner import Summoner

class Map():
    __ALLOWED_TEAMS = ("blue", "red")
    __COUNT = 0
    
    def __init__(self, name, blue=[], red=[]):
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
        if any(type(summoner) is not Summoner for summoner in value):
            raise TypeError("must be a list of summoner")
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
        if any(type(summoner) is not Summoner for summoner in value):
            raise TypeError("must be a list of summoner")
        if len(value) == 5:
            raise ValueError("must be a 5 player in the team")
        self.__blue = value

    def add_summoner(self, summoner, team):
        if team not in Map.__ALLOWED_TEAMS:
            raise TypeError("Team type is not allowed")
        if not isinstance(summoner, Summoner):
            raise TypeError("must be a list of summoner")
        if team == "red":
            self.red.append(summoner)
            if len(self.red) > 5:
                raise ValueError("Too many players in red team")
        if team == "blue":
            self.blue.append(summoner)
            if len(self.blue) > 5:
                raise ValueError("Too many player in blue team")
    
    def __str__(self):
        star_list = 20 * "*"
        print_str = star_list + "\n"
        print_str += "Map name : " + self.name + "\n"
        print_str += "Blue team : \n"
        for s in self.blue:
            print_str += f"\t{s}\n"

        print_str += "\n Red team : \n"
        for s in self.red:
            print_str += f"\t{s}\n"

        print_str += "\n"
        return print_str
