#!/usr/bin/Python3
'''ParmeSean is a webscraper that finds weekly meal prep recipes and emails them to you'''
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup as bs


def scrape_web(url):
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) Chrome/59.0.3071.115'}
    #Some websites don't like being scraped, but including an Agent browser fools the blocker.
    #Thanks StackOverflow
    
    try:
        with closing(get(url, stream=True, headers=agent)) as results: 
        #stream=True means requests cant release the connection until closed
        #closing() closes results at the end of the block

            if html_checker(results):
                return results.content
            # .content() reads HTML off the requests object  
            else:
                return None
    
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def html_checker(results):
    #check if response it html, return true if so
    results_type = results.headers['Content-Type'].lower()
    return (results.status_code == 200
        and results_type is not None
        and results_type.find('html') > -1)

def log_error(e):
    print(e)

#    soup = bs(page.text, "html.parser")
#    results = soup.find_all("span", id="html-attribute-name") #how find element?
#    print(results)
    #content is chosen over .text to avoid problems with character encoding. The second argument ensures
    #that you use the appropriate parser for HTML content




def main():
    url = scrape_web("https://www.tasteofhome.com/recipes/?_cooking-style=easy&_meal-types=lunch")
    if url is not None:
        html = bs(url, "html.parser")
    #sets are iiused over lists as it handles unorganized data better. It only permits unique values
    #data= html.select("script[type=application/ld+json]")

    data= html.find_all("script",type="application/ld+json")


#    print(len(data[1]["name"]))

#recipes.add(data[d]['name'])
#    print(recipes)

#    for s in range(len(data)):
#        if data[s]['name'] == to_find:
#            print(data[s]['name'])

#    keys = ['name']
#    recipes = {x:data[x] for x in keys}

#    for name in data:
#       print(data.keys())
#        data['name']

#    for name in data:
#       data= data.split('\n'
    
    #for rname in html.select('ItemListElement.json()'):
        #print(rname)
        #for each in rname.text.split('\n'):
        #print(
        #return list(recipes)
    #raise Exception('Error retrieving contents at {}'.format(url))



    #print(url)


if __name__ == "__main__":
    main()
