'''Sonia is a webscraper that produces an excel document for easier apartment hunting'''
from bs4 import BeautifulSoup as bs #html parser
import requests
from csv import writer
import time

#grab page data in pure html
def get_url():
    while True:
        url = input("Hi! I'm Sonia, let's scrape some pages. Where are we looking today?\n (Paste URL)")
        url = 'https://www.pararius.com/apartments/amsterdam?ac=1'
        if requests.get(url).status_code == 200:                    #simple url check
            print("HTML retrieved! Time to make some soup")
            time.sleep(1) 
            return requests.get(url)
        else: 
            print("Ooo sorry that URL isn't working right now. Check for typos, or try another URL!")
            time.sleep(1)



def make_soup(page_html): 
    soup = bs(page_html.content, 'html.parser')
    lists = soup.find_all('section', class_='listing-search-item')
    with open("/home/student/static/housing.csv", 'w', newline='') as f:
        ghostwriter = writer(f)
        header = ['Title', 'Subtitle', 'Price', 'Area']
        ghostwriter.writerow(header)
        for list in lists:
            title = list.find('a', class_="listing-search-item__link--title").text.strip().replace('\n','')
            subtitle = list.find('div', class_='listing-search-item__sub-title').text.strip().replace('\n', '')
            price = list.find('div', class_='listing-search-item__price').text.strip().replace('\n', '')
            area = list.find('li', class_='illustrated-features__item--surface-area').text
            info = [title, subtitle, price, area]
            ghostwriter.writerow(info)
            infodict = {
                'Title':title,
                'Subtitle':subtitle,
                'Price':price,
                'Area':area
                }
            print(infodict)

def main():
    page_html = get_url()
    make_soup(page_html)

if __name__ == '__main__':
    main()

#agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) Chrome/59.0.3071.115'}
