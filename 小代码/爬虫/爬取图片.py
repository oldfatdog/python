import urllib.request

f = urllib.request.urlopen('http://placekitten.com/g/200/300') 
content = f.read()
with open('cat_200_300.jpg','wb') as c:
    c.write(content)
