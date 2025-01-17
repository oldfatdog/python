import requests
from bs4 import  BeautifulSoup

json_url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
    }
# 获取几页的搜索结果
for x in range(5):
    params ={
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'txt.yqq.song',
        'searchid': '66451892927258617',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(x+1),
        'n': '10',
        'w': '周杰伦',
        'g_tk_new_20200303': '5381',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }

    res_music = requests.get(json_url,params=params,headers = headers)
    res_music = res_music.json()['data']['song']['list']
    for i in res_music:

        song_url = 'https://y.qq.com/n/yqq/song/'+i['mid']+'.html'
        song_id = i['id']

        headers = {
            'referer':song_url,
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
        }

        lyric_json = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg?nobase64=1&musicid='+str(song_id)+'&-=jsonp1&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
        res_lyric = requests.get(lyric_json,headers = headers)
        res_lyric = res_lyric.json()
        lyric = res_lyric['lyric']

        for i in range(lyric.count('[')):
            left = lyric.find('[')
            right = lyric.find(']')
            lyric = lyric[:left]+'\n'+lyric[right+1:]
        
        lyric = lyric.replace('&#10;','')
        lyric = lyric.replace('&#32;',' ')
        lyric = lyric.replace('&#45;','')
        lyric = lyric.replace('&#40;','')
        lyric = lyric.replace('&#41;','')
        lyric = lyric.strip()

        with open('joy_lyric.txt','a') as l:
            l.write(lyric)
            l.write('\n--------------------------\n')

    print('第%s页歌词写入完成'%(x+1))