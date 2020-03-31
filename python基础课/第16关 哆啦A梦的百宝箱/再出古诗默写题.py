import os

list_test = ['一弦一柱思华年。\n','只是当时已惘然。\n']

with open ('poem1.txt','r',encoding='utf-8') as f:
    lines = f.readlines()

with open('poem_new.txt','w') as new:
    for line in lines:
        if line in list_test:
            new.write('____________。\n')
        else:
            new.write(line)

os.replace('poem_new.txt', 'poem1.txt')
os.getcwd()  # 返回当前工作目录
os.listdir(r'h:\python1\python基础课\第16关 哆啦A梦的百宝箱\再出古诗默写题.py')   # 返回path指定的文件夹包含的文件或文件夹的名字的列表
os.mkdir(path)  # 创建文件夹
os.path.abspath(path)   # 返回绝对路径
os.path.basename(path)   # 返回文件名
os.path.isfile(path)   # 判断路径是否为文件
os.path.isdir(path)   # 判断路径是否为目录