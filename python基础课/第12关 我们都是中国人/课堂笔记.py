#------------------------------------定义类--------------------------------
class Computer:     # 定义类
    screen = True   #电脑共有属性

    def start(self):    #定义类的共有方法
        print('电脑正在开机中……')

my_computer = Computer()    #指定个体属于某个类,类的实例化
print(my_computer.screen)   #得出指定个体的属性
my_computer.start()     #指定个体的方法(能做的事).的意思既是xxx的用法(属性)

#-------代替有两个参数的方法--------
class Chinese:

    name = '吴枫'  # 类属性name

    def say(self, someone):  # 带有两个参数的方法
        print(someone + '是中国人')

person = Chinese()
print(person.name)
person.say('吴枫') 
# self调用时要忽略，'吴枫'传给参数someone

#--------使用self(必须在第一个参数位置)进行内部调用------------------------------------
class Chinese:

    name = '吴枫'  # 类属性name

    def say(self):     
        print(self.name + '是中国人')   #self的作用相当于先给实例占了个位置，等到实例创建好就“功成身退，退位让贤”

person = Chinese()   # 创建Chinese的实例person
person.say()         # 调用实例方法

#----------------在类的方法内部调用其他方法---------
class Chinese:

    def greeting(self):
        print('很高兴遇见你')

    def say(self):
        self.greeting()     #self占坑,等用实例就让给他
        print('我来自中国')

person = Chinese()
# 创建实例person
person.say()
# 调用say()方法

#--------------------------初始化def __init__(self)-------------------------
class Chinese:

    def __init__(self, name, birth, region):
        self.name = name   # self.name = '吴枫' 
        self.birth = birth  # self.birth = '广东'
        self.region = region  # self.region = '深圳'

    def born(self):
        print(self.name + '出生在' + self.birth)

    def live(self):
        print(self.name + '居住在' + self.region)    

person = Chinese('吴枫','广东','深圳') # 传入初始化方法的参数
person.born()
person.live()

class Chinese:
    def __init__(self,hometown):
        self.hometown=hometown
        print('你的家乡来自哪里?')
    def born(self):
        print('我来自{}'. format(self.hometown))
kik=Chinese('湖南')
kik.born()