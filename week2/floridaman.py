#!/usr/bin/python3
import requests
import argparse

url ="https://newsapi.org/v2/top-headlines?country=us&q=+man"
def hollar(newskey):
    thestory = requests.get(f"{url}&apikey={newskey}")
    thestory = thestory.json().keys()
    with open('rawstory.txt', 'w') as f:
        for key, value in thestory.items():
            f.write('%s:%s\n' % (key, value))
    return thestory

def get_title():
    with open('rawstory.txt', 'r') as foo:
        for line in foo:
            if "title" in line:
                print(line)
        
def main():
    try:
        with open('rawstory.txt', 'r') as f:
            mainstory = f
        print("Story Loaded from file!")
    except:
        with open(args.key) as pkey:
            newskey = pkey.read().rstrip('\n') #harvest the key from the file, ignoring empty space to create newskey for use
        mainstory = hollar(newskey)
        print("API Downloaded!")
    get_title()

if __name__ == "__main__":
    parser = argparse.ArgumentParser() #construct a parser
    parser.add_argument('--key', help='Provide the path to the newskey.cred')
    
    args = parser.parse_args() #provides a place to store the parser and its arguments
    main()

