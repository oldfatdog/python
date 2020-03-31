library={'大黄历险记': ['大黄', '很黄很暴力', 1]}
while True:
    require=input('请选择操作?\n存书扣1\n取书扣2\n查书扣3\n退出扣4')
    if require == '1':
        #存放书籍
        input_name=input('书籍名称?')
        for bookname in library:
            if input_name == bookname:
                print('谢谢归还')
            else:
                author=input('书籍作者?')
                recommed=input('推荐语?')
                state = 1
                library[input_name]=[author,recommed,state]
                break
    elif require == '2':
        #取出书籍
        get_name=input('要取出什么书?')
        for bookname in library:
            if get_name == bookname:
                library[get_name][2]=0
                print('已取出书籍')
            else:
                print('查无此书')
    elif require=='3':
        search_name=input('请输入要查询的书本名称')
        for search in library:
            if search_name == search:
                print(library[search_name])
    elif require=='4':
        break
    else:
        print('无效指令')
    print(library)
