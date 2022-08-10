#!/usr/bin/python3
import requests
#open link
nasaapi = "https://api.nasa.gov/planetary/apod?"

def returncreds():
    with open("/home/student/nasa.creds", 'r') as mycreds:
        nasacreds = mycreds.read()

    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

def main():
    #call returncreds to grab the credential
    #make the api get request
    #clean it up by stripping the json
   
    nasacreds = returncreds()
    apicall = requests.get(nasaapi + nasacreds)
    apod = apicall.json()

    print(apod)
    print()
    print(apod["title"] + "\n")
    print(apod["date"] + "\n")
    print(apod["explanation"])
    print(apod["url"])

if __name__ == "__main__":
    main()
