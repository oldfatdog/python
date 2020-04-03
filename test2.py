# 引用requests库
import requests
# 引用BeautifulSoup库
from bs4 import BeautifulSoup

list_all = []
a = 0
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.83 Safari/537.36'}
while a < 226:
    address = 'https://movie.douban.com/top250?start='+str(a)+'&filter='
    # 获取数据
    res_films = requests.get(address,headers=headers)
    # 解析数据
    bs_films = BeautifulSoup(res_films.text,'html.parser')

    # 查找包含菜名和URL的<p>标签
    tag_name = bs_films.find_all('span',class_='title')
    tag_other_name = bs_films.find_all('span',class_='other')

    tag_star = bs_films.find_all('span',class_='rating_num')

    tag_recomed = bs_films.find_all('span',class_='inq')
    # 查找包含食材的<p>标签
    tag_url = bs_films.find_all('div',class_='hd')

    url = []
    for i in tag_url:
        film_url = i.find('a',class_='')
        url.append(film_url['href'])

    for x in range(len(tag_star)):
        full_name = tag_name[x].text+tag_other_name[x].text
        list_film =[full_name,tag_star[x].text,tag_recomed[x].text,url[x]]     # 将信息添加进list_all    
        list_all.append(list_film)

    a = a+25
# 打印
for i in list_all:
    a+=1
    print('排名:'+str(a)+'\n'+'电影名:'+str(i[1])+'\n'+'评分:'+str(i[2])+'\n'+'推荐语:'+str(i[3])+'\n'+'网址:'+str(i[4]))
    print('----------------------------------')