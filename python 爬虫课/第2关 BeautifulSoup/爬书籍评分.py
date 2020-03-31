import requests
from bs4 import BeautifulSoup
res = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
html = res.text
soup = BeautifulSoup(html,'html.parser')
infos = soup.find_all(class_='product_pod')
for info in infos:
    name = info.find('h3')
    book = name.find('a')
    bn = book['title']
    price = info.find(class_='price_color')
    rate = info.find('p')
    star = rate['class']
    final_star = star[1]
    #star = rate['class']
    #final_rate = star[1]
    #price = info.find(class_='price_color')
    print(bn,'\n',price.text,'\n',final_star,'\n')
    #final_rate)
    #print(name.text,'\n',price.text)
