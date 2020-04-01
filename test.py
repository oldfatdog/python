import requests # 调用requests库
from bs4 import BeautifulSoup # 调用BeautifulSoup库




all_img_address = []

res = requests.get('https://boards.4chan.org/wg/thread/7562627')# 返回一个Response对象，赋值给res
html = res.text# 把Response对象的内容以字符串的形式返回
soup = BeautifulSoup( html,'html.parser') # 把网页解析为BeautifulSoup对象
items = soup.find_all(class_="fileThumb")
print(items)


for item in items:
    img_address = item['href']
    all_img_address.append(img_address)

print(all_img_address)
print('已下载全部图片地址')
