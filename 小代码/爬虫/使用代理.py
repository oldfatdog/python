import urllib.request

url = 'https://www.ip.cn/'

proxy_support = urllib.request.ProxyHandler({'http':'58.253.154.187:9999'})

opener = urllib.request.build_opener(proxy_support)

opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.83 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')

print(html)
