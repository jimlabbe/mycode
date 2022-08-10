#!/usr/bin/python3

import requests

url = "http://api.open-notify.org/iss-now.json"

def main():
    rawdata = requests.get(url)
    cleandata = rawdata.json()
    print(cleandata)
# response = requests.get(url).json() will do the same thing
    lon= cleandata["iss_position"]["longitude"]
    lat= cleandata["iss_position"]["latitude"]
    print(f"""
    CURRENT LOCATION
    Longitude: {lon}
    Latitude: {lat}"""
if __name__ == "__main__":
    main()
