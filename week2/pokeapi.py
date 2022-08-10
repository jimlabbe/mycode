#!/usr/bin python3
import requests

# define base URL
URL = "http://pokeapi.co/api/v2/pokemon/"

def main():
    pokemon = requests.get(f"{URL}?limit=1000") #gets 1000 pokemon and makes it into a response object
    pokemon = pokemon.json() #translate the raw data into python readable code

    for poke in pokemon["results"]:
        print(poke.get("name"))

    print(f"Total number of Pokemon returned: {len(pokemon['results'])}")


if __name__ == "__main__":
    main()

