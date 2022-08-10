#!/usr/bin python3
import requests

# define base URL
URL = "http://pokeapi.co/api/v2/item/"

def main():
    items = requests.get(f"{URL}?limit=1000") #gets 1000 pokemon and makes it into a response object
    items = items.json() #translate the raw data into python readable code

    healwords = [] # creating a list to store items with word "heal"

    for item in items.get("results"): #return the list of items mapped to key "results"
        if 'heal' in item.get("name"):
            healwords.append(item.get("name")) #if true, add that item to healwords list
    
    print(f"There are {len(healwords)} words that contain the word heal in the Pokemon Item API")
    print("List of Pokemon items containing heal: ")
    print(healwords)


if __name__ == "__main__":
    main()

