#!/usr/bin/python3
from map import Map
from summoner import Summoner


lucian = Summoner("Lucian", 800, 300)
nami = Summoner("Nami", 600, 600)
jarvan = Summoner("Jarvan", 1500, 300)
shaco = Summoner("Shaco", 800, 800)
bard = Summoner("Bard", 700, 700)
garen = Summoner("Garen", 1200, 300)
velkoz = Summoner("Velkoz", 800, 1000)
jax = Summoner("Jax", 1000, 400)
janna = Summoner("Janna", 700, 700)
vayne = Summoner("Vayne", 700, 300)

"""for s in [lucian, nami, jarvan, shaco, bard]:
    ranked.add_summoner(s, "blue")
for s in [garen, velkoz, jax, janna, vayne]:
    ranked.add_summoner(s, "red")"""

ranked = Map("Summoner's Rift", [lucian, nami, jarvan, shaco, bard] ,[garen, velkoz, jax, janna, vayne])

print(ranked)
