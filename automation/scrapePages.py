import requests
from bs4 import BeautifulSoup
url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_ = 'col-lg-4 col-md-6 mb-4')
count = 1
for i in items:
    ItemName = i.find('h4', class_ ='card-title').text.strip('\n')
    ItemPrice = i.find('h5').text
    print('%s ) Price: %s, ItemName: %s' % (count, ItemPrice, ItemName))
    count = count + 1

# with this code you can scrape from a shopping page example and extract all the useful items from it
# and even farther can scrape multiple pages

pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')
# at this point we check if the links are valid
# and not linked to next or previous page
# for this purpose we have to convert it to
# integer first else we get None value
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get('href')
        urls.append(x)
# print(urls)
# count = 1
for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in items:
        ItemName = i.find('h4', class_ ='card-title').text.strip('\n')
        ItemPrice = i.find('h5').text
        print('%s ) Price: %s, ItemName: %s' % (count, ItemPrice, ItemName))
        count = count + 1