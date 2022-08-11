#!/usr/bin/python3
import requests
import argparse
import pandas

url ="https://newsapi.org/v2/top-headlines?country=us&q=+man&"
def hollar(newskey):
    thestory = requests.get(f"{url}&apikey={newskey}")
    thestory = thestory.json()
    return thestory

def main():
    with open(args.key) as pkey:
       newskey = pkey.read().rstrip('\n') #harvest the key from the file, ignoring empty space to create newskey for use
    hollar(newskey)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser() #construct a parser
    parser.add_argument('--key', help='Provide the path to the newskey.cred')
    
    args = parser.parse_args() #provides a place to store the parser and its arguments
    main()
