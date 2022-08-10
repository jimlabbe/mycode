#!/usr/bin python3
import requests
import argparse 
import pandas

# define base URL
URL = "http://pokeapi.co/api/v2/item/"

def main():
    items = requests.get(f"{URL}?limit=1000") # this is a request, in JSON
    #gets 1000 pokemon and makes it into a response object

    items.dict = items.json() #translate the raw data into python readable code, stored as a dictionary
    matches = {"matched":[]} # creating a list to store items with the word that was searched for
    for item in items.get("results"): 
    # loop over the data and return the list of items mapped to key "results"
        if args.searchword in item.get("name"): 
        # check if current items value mapped to item name that contains the search word
            matches["matched"].append(item["name"]) 
            #if true, add that item to matchedwords list

    finishedlist = matchedwords.copy() 
    #maps the list of matched words to a dict called matched words
    matchedwords = {}
    matchedwords["matched"] = finishedlist
    print(matchedwords) 
    #export to excel with pandas and makes a datafrom from our data
    itemsdf = pandas.DataFrame(matchedwords)

   # export to MS Excel XLSX format
    itemsdf.to_excel("pokemonitems.xlsx", index=False)

    print("Gotta catch 'em all!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pass in a word to search to Pokemon item API")
    #create a parser object that can create arguments at the command line
    

    #lets teach it what arguments to recognize. Dashes indicate an optional argument
    #the type of searchword is being set to string here. otherwise, the default 
    #searchword is ball. help just tells us details about the parser
    parser.add_argument('--searchword', metavar='SEARCHW', type=str, default='ball', help="Pass in any word. Default is 'ball' ")
    
    args = parser.parse_args() 
    #this args object holds whatever was typed in at the command line
    main()

