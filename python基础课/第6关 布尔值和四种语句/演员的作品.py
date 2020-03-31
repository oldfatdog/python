movies = {
'妖猫传':['黄轩','染谷将太'],
'无问西东':['章子怡','王力宏','祖峰'],
'超时空同居':['雷佳音','佟丽娅'],
}

actor = input('input actor ')
for movie in movies:    #遍历电影名字(键值),每找一个电影往下循环一次
    actors = movies[movie]  #找到电影名字对应的演员(值)
    if actor in actors:
        print(actor +'was in'+movie )
