import os
import easygui as eg

python_file_list = []

def search_file(start_dir):
    os.chdir(start_dir)
    for each_file in os.listdir(os.curdir):
        if os.path.isfile(each_file):
            file_ext = os.path.splitext(each_file)[1]
            if file_ext in ['.py']:
                python_file_list.append(os.getcwd() + os.sep + each_file + os.linesep)
        if os.path.isdir(each_file):
            search_file(each_file)  # 递归调用
            os.chdir(os.pardir)  # 递归调用后切记返回上一层目录
    return python_file_list

def selet_search_address():
    msg = '选择存放代码的文件夹'
    title = '代码统计'
    search_adress = eg.diropenbox(msg,title)
    return search_adress

search_file(selet_search_address())
print(python_file_list)

new_file_list = []
for filename in python_file_list:
    str1 = filename[:-2]
    new_file_list.append(str1)
print(new_file_list)

lines = 0

for eachfile in new_file_list:
    with open(eachfile,'r',encoding='utf-8') as file:
        content = file.readlines()
        lines = lines + len(content)

percent = (lines/100000)*100
remain = 100000 - lines
msg = '您目前共累积编写了%s行代码,完成进度:%s%%\n离10万行代码还差%s行,请继续努力'%(lines,percent,remain)
title = '代码统计'
eg.msgbox(msg,title)