#!/usr/bin/python3

class Neighborhood:
    __neighborhood_count = 0
    def __init__(self):
        Neighborhood.__neighborhood_count += 1
    @property
    def neighborhood_count(self):
        return self.__neighborhood_count
    
    def get_count():
        return Neighborhood.__neighborhood_count

    def __del__(self):
        Neighborhood.__neighborhood_count -= 1
    
class Daycare:
    def __init__(self, animals):
        self.animals = animals

    def __str__(self):
        animnum = 0
        eighthash = "#" * 8
        who = "Who's in there? \n"
        for animal in self.__animals:
            who += "Animal: " + str(animnum) + " " + animal.name + "\n"
            animnum += 1

        return who
    @property
    def animals(self):
        return self.__animals
    @animals.setter
    def animals(self, animals):
        if not isinstance(animals, list):
            raise TypeError("Not a list")
        if not all(type(animal) is Animal for animal in animals):
            raise TypeError("must be a list of animal")
        
        self.__animals = animals
        
class Animal:

    __VALID_SPECIES = ("dog", "cat", "bird")
    __SPEECH = {"dog": "woof woof: My name is ",
                "cat": "meow meow: My name is ",
                "bird": "tweet tweet: My name is "
                }
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __add__(self, animal):
        return Daycare([self, animal])

    def __str__(self):
        fullstring = ""
        fullstring += self.__SPEECH[self.__species] + self.__name
        return fullstring
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def species(self):
        return self.species
    
    @species.setter
    def species(self, species):
        if species not in self.__VALID_SPECIES:
            raise ValueError("not a species")
        self.__species = species
def create():
        n2 = Neighborhood()
        n3 = Neighborhood()
        print("all neghborhood: {}".format(Neighborhood.get_count()))

if __name__ == "__main__":
    n1 = Neighborhood()
    print("all neghborhood: {}".format(Neighborhood.get_count()))
    
    create()
    
    print("all neighbor: {}".format(Neighborhood.get_count()))
    cat = Animal("harry", "cat")
    dog = Animal("penny", "dog")
    print(dog)
    print(cat)
