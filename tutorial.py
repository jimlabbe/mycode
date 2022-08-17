from bs4 import BeautifulSoup as bs
import requests
from csv import writer


url = 'https://www.pararius.com/apartments/amsterdam?ac=1'
page = requests.get(url)
 
soup = bs(page.content, 'html.parser')
lists = soup.find_all('section', class_='listing-search-item')
print(lists)
with open("/home/student/static/housing.csv", 'w', newline='') as f:
    ghostwriter = writer(f)
    header = ['Title', 'Subtitle', 'Price', 'Area']
    ghostwriter.writerow(header)
    for list in lists:
        title = list.find('a', class_="listing-search-item__link--title").text
        subtitle = list.find('div', class_='listing-search-item__sub-title').text
        price = list.find('div', class_='listing-search-item__price').text
        area = list.find('li', class_='illustrated-features__item--surface-area').text
        info = [title, subtitle, price, area]
        ghostwriter.writerow(info)

#agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) Chrome/59.0.3071.115'}
