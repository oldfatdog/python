with open(r'pythontest\photo1.png','rb') as file:
    filecontent = file.read()

with open(r'photo1copy.png','wb') as photo1copy:
    photo1copy.write(filecontent)
