file1 = open(r'test\scores.txt','r',encoding='utf=8')
file1_content=file1.readlines()
print(file1_content)

final_score=[]

for i in file1_content:
    data=i.split()
    print(data)

    sumption=0
    for score in data[1:]:
        sumption = sumption+int(score)

    result=data[0]+str(sumption)
    print(result)


------------计算一个总分写一下总分-------------------

    winner = open(r'test\winner.txt','a',encoding='utf=8')
    winner.writelines(result+'\n')
    winner.close()


------------------全部算好了一起写进去----------------


    final_score.append(result)
print(final_score)

winner = open(r'test\winner.txt','w',encoding='utf=8')
winner.writelines(final_score)
winner.close()


