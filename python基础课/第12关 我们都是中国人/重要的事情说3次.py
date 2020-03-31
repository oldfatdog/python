# 这个代码只要用到类中的初始化方法和类的实例化。
# 在完成代码后，请复制到你的本地（下一步要用）。
class Robot:
    def __init__(self,my_name,ro_name):
        self.mname=my_name
        self.rname=ro_name
        print('我是机器人{},你好{}'.format(self.rname,self.mname))

    def say_wish(self):
        wish=input('说出你的愿望吧骚年')
        print(self.mname+'的愿望是')
        for i in range(3):
            print(wish)

walle=Robot('猫猫','狗狗')
walle.say_wish()

#--------------------参考答案--------------
class Robot:
    def __init__(self):
        self.name = input('我现在刚诞生，还没有名字，帮我起一个吧。')
        self.master = input('对了，我要怎么称呼你呢？')
        print('你好%s，我叫%s。很开心，遇见你~'%(self.master,self.name))
    
    def say_wish(self):
        wish = input('告诉一个你的愿望吧：')
        print(self.master+'的愿望是：')
        # 这里也可以用字符串的格式化，不过，用循环语句的话，之后改复述次数会方便些。
        for i in range(3):
            print(wish)

robot1 = Robot()
robot1.say_wish()
