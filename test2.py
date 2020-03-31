import urllib.request
import urllib.parse

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data ={}
data['i']='apple'
data['from']= 'AUTO'
data['to']= 'AUTO'
data['smartresult']= 'dict'
data['client']= 'fanyideskweb'
data['salt']= '15855504909729'
data['sign']= '40c07c62b7f93e30ebe6d45ae8759686'
data['ts']= '1585550490972'
data['bv']= '616f168e24ef150e4dad986839af2ac3'
data['doctype']= 'json'
data['version']= '2.1'
data['keyfrom']= 'fanyi.web'
data['action']= 'FY_BY_REALTlME'
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
print(html)