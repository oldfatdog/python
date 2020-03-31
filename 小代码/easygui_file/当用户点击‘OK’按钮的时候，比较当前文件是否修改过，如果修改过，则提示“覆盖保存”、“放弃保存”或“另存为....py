import easygui as eg
import os

file_type = ["*.txt"]
default_address = "C:\\Users\\huang\\Desktop\\python\\*.txt" 

file_address = eg.fileopenbox(filetypes=file_type,default=default_address)

with open(file_address,'r',encoding='utf-8') as txt:
    content = txt.read()
    title = file_address
    msg = '文件【%s】的内容如下：' % title
    contenr_after = eg.textbox(msg,title,content)

if content == contenr_after:
    choice = ["覆盖保存", "放弃保存", "另存为"]
    msg = "覆盖保存", "放弃保存", "另存为"
    title = '警告'
    choose = eg.buttonbox(msg,title,choice)
    if choose == '覆盖保存':
        with open(file_address) as file:
            file.write(contenr_after[:-1])
    elif choose == "另存为":
        msg = '选择保存路径'
        title = '保存文件'
        default = default_address
        file_save_address = eg.filesavebox(msg,title,default)
        file_name = os.path.basename(file_address)
        with open(file_name,'w') as new_file:
            new_file.write(contenr_after[:-1])
    else:
        pass

