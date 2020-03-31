i=1
list={}
while True:
    a = input('A，你认罪吗？请回答认罪或者不认：')
    b = input('B，你认罪吗？请回答认罪或者不认：')
    # 需要将每一对实验者的选择存起来。

    if a == '认罪' and b == '认罪':
        print('两人都得判10年，唉')
    elif a == '不认' and b == '认罪':
        print('A判20年，B判1年，唉')
    elif a == '认罪' and b == '不认':
        print('A判1年，B判20年')
    else:
        print('都判3年，太棒了')
    if a == '不认' and b == '不认':
        print('第'+str(i)+'组做出了最优选择')
    list.update({i:[a,b]})
    print(list)
    i=i+1
    if input('是否结束？') == '是':
        break
print(list)