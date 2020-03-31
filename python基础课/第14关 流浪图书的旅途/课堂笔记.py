class Book:

    def __init__(self, name, author, comment, state = 0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state

    def __str__(self):      #__str__(self)方法，那么当使用print打印实例对象的时候，就会直接打印出在这个方法中return的数据
        if self.state == 0:
            status = '未借出'
        else:
            status = '已借出'
        return '名称：《%s》 作者：%s 推荐语：%s\n状态：%s ' % (self.name, self.author, self.comment, status)

book1 = Book('像自由一样美丽','林达','你要用光明来定义黑暗，用黑暗来定义光明')
# 传入参数，创建实例对象
print(book1)
# 直接打印对象即可，不能写成print(book1.__str__())