import random
import json
from Type import Type 
from pokemon import Pokemon
import time

class Combat(Type, Pokemon):
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def liste_pokemon(self):
        with open('pokemon.json') as f:
            data = json.load(f)
            pokemons = data['pokemons']
            for pokemon_data in data['pokemons']:
                pokemon = Pokemon(
                    pokemon_data['nom'],
                    pokemon_data['level'],
                    pokemon_data['defense'],
                    pokemon_data['PV'],
                    pokemon_data['puissance'],
                    pokemon_data['type']
                )
                pokemons.append(pokemon)
            return pokemons

    def aleatoire(self):

        multiplicateur = {
        "Eau": {"Eau": 1, "Feu": 0.5, "Terre": 2, "Normal": 0.75},
        "Feu": {"Eau": 2, "Feu": 1, "Terre": 0.5, "Normal": 0.75},
        "Terre": {"Eau": 0.5, "Feu": 2, "Terre": 1, "Normal": 0.75},
        "Normal": {"Eau": 0.75, "Feu": 0.75, "Terre": 0.75, "Normal": 0.75},
        }
        while self.pokemon1._PV > 0 and self.pokemon2._PV > 0:
            if random.randint(0, 1) == 1:
                if self.pokemon1.type in multiplicateur and self.pokemon2.type in multiplicateur[self.pokemon1.type]:
                    multiplicateur_attaque = multiplicateur[self.pokemon1.type][self.pokemon2.type]
                    degats = ( self.pokemon1.puissance * multiplicateur_attaque ) / 2
                else:
                    multiplicateur_attaque = 1
                if random.randint(0, 10) > 2:  # Probabilité de 80% pour une attaque réussie
                    degats = ( self.pokemon1.puissance * multiplicateur_attaque ) / 2
                    print(f"{self.pokemon1._nom} attaque avec un multiplicateur de {multiplicateur_attaque} contre {self.pokemon2._nom}")
                    if degats < 0:
                        degats = 0
                    self.pokemon2._PV -= degats
                    print(f"{self.pokemon1._nom} a infligé {degats} points de dégâts à {self.pokemon2._nom}")
                else:  # 20% de probabilité pour une attaque ratée
                    print(f"{self.pokemon1._nom} a raté son attaque contre {self.pokemon2._nom}")
                if self.pokemon2._PV > 0:
                    if self.pokemon2.type in multiplicateur and self.pokemon1.type in multiplicateur[self.pokemon2.type]:
                        multiplicateur_attaque = multiplicateur[self.pokemon2.type][self.pokemon1.type]
                        degats = ( self.pokemon1.puissance * multiplicateur_attaque ) / 2
                    else:
                        multiplicateur_attaque = 1 
                        
                    if random.randint(0, 10) > 2:  # Probabilité de 80% pour une attaque réussie
                        degats =  ( self.pokemon2.puissance * multiplicateur_attaque ) / 2
                        print(f"{self.pokemon2._nom} attaque avec un multiplicateur de {multiplicateur_attaque} contre {self.pokemon1._nom}")
                        if degats < 0:
                            degats = 0
                        self.pokemon1._PV -= degats
                        print(f"{self.pokemon2._nom} a infligé {degats} points de dégâts à {self.pokemon1._nom}")
                    else:  # 20% de probabilité pour une attaque ratée
                        print(f"{self.pokemon2._nom} a raté son attaque contre {self.pokemon1._nom}")
    
        



                

    def enVie(self):
        if self.pokemon1._PV <= 0:
            print(f"{self.pokemon1._nom} est mort") 
            print(f"{self.pokemon2._nom} a gagné" )
        else:
            print(f"{self.pokemon1._nom} a encore {self.pokemon1._PV} points de vie")
                  
        if self.pokemon2._PV <= 0:
            print(f"{self.pokemon2._nom} est mort")
            print(f"{self.pokemon1._nom} a gagné")
        else:
            print(f"{self.pokemon2._nom} a encore {self.pokemon2._PV} points de vie")

    def combat(self):
        num_tours = 0
        while self.pokemon1._PV > 0 and self.pokemon2._PV > 0 and num_tours < 100:
            self.aleatoire()
            time.sleep(1)
            if self.pokemon1._PV <= 0 or self.pokemon2._PV <= 0:
                self.enVie()
                break  
            num_tours += 1

