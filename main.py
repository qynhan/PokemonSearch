import requests

def getPokemon(pokemonName):
    baseURL = "https://pokeapi.co/api/v2/"
    response = requests.get(f"{baseURL}pokemon/{pokemonName}")
    if response.status_code == 200:
        return response.json()
    else:
        print("invalid pokemon name!")

pokemonSearch = "pikachu"
pokemonInfo = getPokemon(pokemonSearch)
print("Pokemon Name: ", pokemonInfo["name"])
print("Pokemon Weight: ", pokemonInfo["weight"])
print("Pokemon number of moves: ", len(pokemonInfo["moves"]))