import requests
from bs4 import BeautifulSoup
# a simple web scraper
# url = 'http://bahramzade.ir'
url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
# print(soup)
# useful items for scraping coming from BODY portion of the HTML
# based on html format we found that the type is as below span and class = text
quotes = soup.find_all('span', class_ = 'text')
authors = soup.find_all('small', class_ = 'author')
tags = soup.find_all('div', class_ = 'tags')
# now to have all of them in text we should use .text method with for loop to iterate through the items
# 1 for quote in quotes:
# 1    print(quote.text)
# 2 since all are one on one so we use for loop for each items
for i in range(0,len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a', class_ = 'tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)

# this is where world of web scraping is open now