import urllib.request
import os
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def find_imgs(url):
    html = open_url(url).decode('utf-8')
    p = r'<a href="([^"]+.(?:jpg|gif))"'
    pic_list = re.findall(p, html)
    return pic_list
   

def get_next_page(url):
    html = open_url(url).decode('utf-8')
    p = r'<a title="Older Comments" href="([^"]+)"'
    _result = re.search(p, html)
    new_url = 'https:' + _result.group(1)
    return new_url

def sava_imgs(pic_list):
    for each in pic_list:
        filename = each.split('/')[-1]
        each = 'https:' + each
        urllib.request.urlretrieve(each,filename)

def g_pic_dl(folder='妹子图',pages=5):
    pic_list = []
    url = "https://jandan.net/ooxx"
    if os.path.isdir(folder) == 0:
        os.mkdir(folder)
    os.chdir(folder)
    while pages > 0:
        pic_list=find_imgs(url)
        sava_imgs(pic_list)
        url = get_next_page(url)
        pages -= 1

if __name__ == '__main__':
    g_pic_dl()