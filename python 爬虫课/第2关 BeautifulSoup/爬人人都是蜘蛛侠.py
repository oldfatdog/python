import requests
from bs4 import BeautifulSoup
res = requests.get('https://spidermen.cn')
html = res.text
soup = BeautifulSoup(html,'html.parser')
infos = soup.find_all(class_='entry-header')
for info in infos :
    time = info.find('time')
    title = info.find(class_='entry-title')
    link = title.find('a')
    lian_jie = link['href']
    print(time.text,'\n',title.text,'\n',lian_jie,'\n')