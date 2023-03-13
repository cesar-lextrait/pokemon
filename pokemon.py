import json

with open('pokemon.json') as f:
    # Load the JSON data
    data = json.load(f)

# Access the list of pokemons
pokemons = data['pokemons']


class Pokemon:
    def __init__(self, nom, level, defense, PV, puissance, type):
        self._nom = nom
        self._PV = float(PV)
        self.level = level
        self.puissance = puissance
        self.defense = defense 
        self.type = type

    def estVivant(self):
        return self._PV > 0
    
    def afficherInfos(self):
        print(f"Nom : {self._nom}")
        print(f"PV : {self._PV}")
        print(f"Level : {self.level}")
        print(f"Puissance : {self.puissance}")
        print(f"Défense : {self.defense}")
        print(f"Type : {self.type}")


pokemons = []
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
