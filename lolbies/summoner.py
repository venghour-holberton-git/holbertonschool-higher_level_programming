#!/usr/bin/python3

class Summoner:
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.team = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, value):
        self.__mana = value
    
    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value
    
    @property
    def team(self):
        return self.__team

    @team.setter
    def team(self, value):
        self.__team = value

    def q_spell(self):
        pass

    def w_spell(self):
        pass

    def e_spell(self):
        pass

    def r_spell(self):
        pass

    def __str__(self):
        return f"{self.name}\tHP: {self.hp:<8}Mana: {self.mana:<8} Team: {self.team}"
