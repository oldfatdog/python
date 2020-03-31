sent='锦瑟无端五十弦，'
repl='aaaaa'

with open('poem1.txt','r',encoding='utf-8') as poem:
	content = poem.readlines()

result=[]
for i in range(len(content)):
    tran=content[i]
    tran1=tran.replace(sent,repl)
    print(tran1)
    result.append(tran1)

with open('reult.txt','w',encoding='utf-8') as poem2:
	poem2.writelines(result)

