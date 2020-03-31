import urllib.request
import urllib.parse
import json

content = input('请输入需要翻译的内容:')

head = {}
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.83 Safari/537.36' 

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data ={}
data['i']=content
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

req = urllib.request.Request(url,data,head)

# 第二种添加header的方式,要去掉Request括号中的head
# req.addheaders('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.83 Safari/537.36')

html = urllib.request.urlopen(req)
html = html.read().decode('utf-8')

target = json.loads(html)
print('翻译结果:%s'%(target['translateResult'][0][0]['tgt']))
