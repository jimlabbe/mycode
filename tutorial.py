import requests
import json
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer

url = 'https://www.tasteofhome.com/recipes/?_cooking-style=easy&_meal-types=lunch'
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) Chrome/59.0.3071.115'}
r = requests.get(url, headers=agent)
only_s_tags = SoupStrainer("script")

soup = bs(r.content, 'html.parser', parse_only=only_s_tags)
print(soup.decompose())


#script = soup.find_all("script",type="application/ld+json").text()
#print(type(script))
#data = json.loads(script)
#print(data)
#print(data['itemListElement'][0])

