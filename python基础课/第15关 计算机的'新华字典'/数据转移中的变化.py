# 下面已经为你准备好了打开的代码和一些变量名的准备。
# 请你完成数据处理以及新建文档（同一个目录）的代码。
# 一个提示：可以用 print 作为检验代码，步步为营。
'''            
dict_scores = {}
list_scores = []
final_scores = []         
            
file1 = open('winner.txt','r',encoding='utf-8') 
file_lines = file1.readlines() 
file1.close()
print(file_lines)
#------把原始数据转成字典-----------
for i in file_lines:    
    word=[]
    number=[]
    for j in i:
        try:
            int(j)
            number.append(j)
        except ValueError:
            word.append(j)
    word=word[:-1]
    empty=''
    word_combine=empty.join(word)
    number_combine=empty.join(number)
    dict_scores[word_combine]=int(number_combine)
    
for i in range(len(dict_scores))
    for key in dict_scores:
    	if dict_scores[key]
    
    
    print(word_combine)
    print(number_combine)
    print(dict_scores)
       '''

# =======================以下参考答案========================
# 下面注释掉的代码，皆为检验代码（验证每一步的思路和代码是否达到目标，可解除注释后运行）。

file1 = open(r'D:\python1\test\winner.txt','r',encoding='utf-8') 
file_lines = file1.readlines() 
file1.close()

dict_scores = {}
list_scores = []
final_scores = []

# print(file_lines) 
# print(len('\n'))

# 打印结果为：['罗恩102\n', '哈利383\n', '赫敏570\n', '马尔福275\n']
# 经过测试，发现'\n'的长度是1。所以，名字是“第0位-倒数第5位”，分数是“倒数第4位-倒数第二位”。
# 再根据“左取右不取”，可知：name-[:-4],score-[-4:-1]

for i in file_lines:  # i是字符串。
    print(i)
    name = i[:-4]  # 取出名字（注：字符串和列表一样，是通过偏移量来获取内部数据。）
    score = int(i[-4:-1])  # 取出成绩
    print(name)
    print(score)
    dict_scores[score] = name  # 将名字和成绩对应存为字典的键值对(注意：这里的成绩是键)
    list_scores.append(score)

# print(list_scores)
list_scores.sort(reverse=True)  # reverse，逆行，所以这时列表降序排列，分数从高到低。
# print(list_scores)

for i in list_scores:
    result = dict_scores[i] + str(i) + '\n'
    # print(result)
    final_scores.append(result)

print(final_scores)  # 最终结果

winner_new = open('winner_new.txt','w',encoding='utf-8') 
winner_new.writelines(final_scores)
winner_new.close()
