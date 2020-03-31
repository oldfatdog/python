class Book:     #提供书的信息
 
    def __init__(self, name, author, comment, state = 0):       #初始化个体信息(例如游戏开始时的角色名称/性别)
        self.name = name        #把初始录入的个体信息(参数)记录下来以便以后使用
        self.author = author
        self.comment = comment
        self.state = state
 
    def __str__(self):      #自带__str__方法,print个例可直接打印出返回值
        status = '未借出'
        if self.state == 1:
            status = '已借出'
        return '名称：《%s》 作者：%s 推荐语：%s\n状态：%s ' % (self.name, self.author, self.comment, status)

class BookManager:      #对书进行增删改查

    books = []      #定义书的存放列表

    def __init__(self):     #初始化书架,里面存了3本书,其中一本已被借走
        book1 = Book('惶然录','费尔南多·佩索阿','一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book('以箭为翅','简媜','调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手','卡森·麦卡勒斯','我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。',1)
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)

    def menu(self):     #用户操作界面程序
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while True:     #有条件的无限循环
            print('1.查询所有书籍\n2.添加书籍\n3.借阅书籍\n4.归还书籍\n5.退出系统\n')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_all_book()
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lend_book()
                break

    def show_all_book(self):
        for book in self.books:     #遍历book信息并打印
            print(book)
            print('')
    
    def add_book(self):         #增加书籍
        new_name = input('请输入书籍名称：')
        new_author = input('请输入作者：')
        new_comment = input('请输入推荐语：')
        new_book=Book(new_name,new_author,new_comment)      #新书要分到book类中才会有整本书的状态
        self.books.append(new_book)
        print('书籍录入成功')
    def check_book(self,name):
        for book in self.books:
            if book.name == name:
                 return book 
        else:
            return None

    def lend_book(self):
        name = input('请输入借阅书籍的名称：')
        res = self.check_book(name)

        if res != None:
            if res.state == 1:
                print('你来晚了一步，这本书已经被借走了噢')
            else:
                print('借阅成功，借了不看会变胖噢～')
                res.state = 1
        else:
            print('这本书暂时没有收录在系统里呢')

    def return_book(self):
        name = input('请输入归还书籍的名称：')
        result=self.check_book(name)
        if result != None:
            result.state == 0
            print('感谢归还')
        else:
            print('这书不是在我们这借的吧?')


manager = BookManager()
manager.menu()


