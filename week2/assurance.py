import requests

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
term = input("What terms do you want to search for")

querystring = {"term":term}

headers = {
	"X-RapidAPI-Key": "892de4c27emshad4b4cb9ef04c09p17acecjsn933c7eb59b5a",
	"X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
