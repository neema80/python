import requests
from bs4 import BeautifulSoup
url = 'https://www.digikala.com/search/category-mobile-phone/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_ = 'c-product-box__content')
# bug TODO:
# prices = soup.find_all('div', class_ = 'c-price__value-wrapper')
#for link in soup.find_all('a'):
#    if link.has_attr('href'):
#        print(link.attrs['href'])

count = 1
for i in items:
    ItemName = i.find('a').text
    ItemPrice = i.find('div', class_ = 'c-price__value-wrapper').text.strip('\u06f4')
    print("{} ) Price: {}, ItemName: {}".format(count, ItemPrice, ItemName))
    #file = open('scrape.txt',"w")
    #file.write(sample)
    #file.close()
    count = count + 1

# with this code you can scrape from a shopping page example and extract all the useful items from it
# and even farther can scrape multiple pages
