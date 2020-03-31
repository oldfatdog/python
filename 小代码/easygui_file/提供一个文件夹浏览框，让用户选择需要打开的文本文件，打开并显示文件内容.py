import easygui as eg

file_type = ["*.txt"]
default_address = "C:\\Users\\huang\\Desktop\\python\\*.txt" 

file_addres = eg.fileopenbox(filetypes=file_type,default=default_address)

with open(file_addres,'r',encoding='utf-8') as txt:
    content = txt.read()
    print(content)
    eg.textbox(content,title='文本内容')