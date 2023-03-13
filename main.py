from pokemon import Pokemon
from combat import Combat
import random
import json
import time

with open('pokemon.json') as f:
    data = json.load(f)


with open('pokemon.json') as f:
    data = json.load(f)
pokemon_list = []
for pokemon_data in data['pokemons']:
    pokemon = Pokemon(pokemon_data['nom'], pokemon_data['level'], pokemon_data['defense'], pokemon_data['PV'], pokemon_data['puissance'], pokemon_data['type'])
    pokemon_list.append(pokemon)

liste_pokemon = ["Pikachu", "Bulbizarre", "Salameche", "Carapuce"]

print("Bienvenue dans le jeu Pokemon")
print("1. Jouer")
print("2. Quitter")
choix = input("Que voulez-vous faire ? 1 pour jouer 2 pour quitter ")
if choix == "1":
    pokemon1 = input(f"Choisissez votre premier pokemon parmi {', '.join(liste_pokemon)} ")
    if pokemon1 in liste_pokemon:
        print("Vous avez choisi : ", pokemon1)
        pokemon2 = random.choice(pokemon_list)
        print("Votre adversaire a choisi ", pokemon2._nom)
        print("Premier combat !")
        pokemon1 = pokemon_list[liste_pokemon.index(pokemon1)]
        pokemon2 = pokemon2
        combat = Combat(pokemon1, pokemon2)
        combat.combat()
        time.sleep(1)
    else:
        print("Ce pokemon n'existe pas")
