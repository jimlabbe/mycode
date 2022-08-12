#!/usr/bin/Python3
'''ParmeSean is a webscraper that finds weekly meal prep recipes and emails them to you'''
import requests
from bs4 import BeautifulSoup as bs


def scrape_web():
    url = "https://www.tasteofhome.com/recipes/1/?_cooking-style=easy&_meal-types=lunch"
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) Chrome/59.0.3071.115'}
    #Some websites don't like being scraped, but including an Agent browser fools the blocker.
    #Thanks StackOverflow

    page = requests.get(url, headers=agent) #requests the page data
    soup = bs(page.content, "html.parser")
    results = soup.find_all("span", id="html-attribute-name") #how find element?
    print(results)
    #content is chosen over .text to avoid problems with character encoding. The second argument ensures
    #that you use the appropriate parser for HTML content





def main():
    scrape_web()
# scrape the website

# email the results

# monitor an inbox


if __name__ == "__main__":
    main()
