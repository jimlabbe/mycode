#!/usr/bin/env python3

import urllib.request
import json

majortom = "http://api.open-notify.org/astros.json"

def main():
    '''reading json from api'''

    groundctrl = urllib.request.urlopen(majortom)

    helmet = groundctrl.read()

    print(helmet)

    helmetson = json.loads(helmet.decode("utf-8"))

    print(type(helmet))

    print(type(helmetson))

    print(helmetson["number"])

    print(helmetson["people"])

    print(helmetson["people"][0])
    
    print(helmetson["people"][1])


    print(helmetson["people"][-1])

    for astro in helmetson["people"]:
        print(astro)
    for astro in helmetson["people"]:
        print(astro["name"])

if __name__ == "__main__":
    main()

