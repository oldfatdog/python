# ==========================类的继承===========================
class Chinese:
    eye = 'black'

    def eat(self):
        print('吃饭，选择用筷子。')

class Cantonese(Chinese):  
# 通过继承，Chinese类有的，Cantonese类也有
    pass

# 验证子类可以继承父类的属性和方法，进而传递给子类创建的实例
yewen = Cantonese()  
# 子类创建的实例，从子类那间接得到了父类的所有属性和方法
print(yewen.eye)  
# 子类创建的实例，可调用父类的属性
yewen.eat()  
# 子类创建的实例，可调用父类的方法

#-----------------函数isinstance()，可以用来判断某个实例是否属于某个类----------

print(isinstance(1,int))
# 判断1是否为整数类的实例
print(isinstance(1,str))

print(isinstance(1,(int,str)))
# 判断实例是否属于元组里几个类中的一个
#------------------
class Chinese:
    pass

class Cantonese(Chinese):
    pass

gonger = Chinese()
# 宫二，电影《一代宗师》女主，生于东北
yewen = Cantonese()
# 叶问，电影《一代宗师》男主，生于广东

print('\n验证1：子类创建的实例同时也属于父类')
print(isinstance(gonger,Chinese))  
print(isinstance(yewen,Chinese))  

print('\n验证2：父类创建的实例不属于子类。')
print(isinstance(gonger,Cantonese))

print('\n验证3：类创建的实例都属于根类。')
print(isinstance(gonger,object))  
print(isinstance(yewen,object))

#=========================类的多层继承与多重继承=================
# class a(b),class c(a);class a(b,c,d)
# class Yuesu(Yue,Su)括号里Yue和Su的顺序是有讲究的。和子类更相关的父类会放在更左侧。
# 我认为“出生在江苏，定居在广东的人”在穿着和饮食等方面会更接近广东人，所以将 Yue 放在 Su 的左侧。
# 广东人创建的实例在调用属性和方法时，会先在左侧的父类中找，找不到才会去右侧的父类找。（可理解为“就近原则”）

class Su:
    born_city = 'Jiangsu'
    wearing = 'thick'  # 穿得较厚

    def diet(self):
        print('我们爱吃甜。')

class Yue:
    settle_city = 'Guangdong'
    wearing = 'thin'  # 穿得较薄

    def diet(self):
        print('我们吃得清淡。')

class Yuesu(Yue,Su):
    pass

xiaoming = Yuesu()
print(xiaoming.wearing)
print(xiaoming.born_city)
xiaoming.diet()

#===================================类的定制===========================
class Chinese:
    eye = 'black'

    def eat(self):
        print('吃饭，选择用筷子。')

class Cantonese(Chinese):  # 类的继承
    native_place = 'guangdong'  # 类的定制

    def dialect(self):  # 类的定制
        print('我们会讲广东话。')

yewen = Cantonese()
print(yewen.eye)
# 父类的属性能用
print(yewen.native_place)
# 子类的定制属性也能用
yewen.eat()
# 父类的方法能用
yewen.dialect()
# 子类的定制方法也能用

#----------------------继承父类方法再调整---------------

class Chinese:

    def land_area(self,area):
        print('我们居住的地方，陆地面积是%d万平方公里左右。'% area)

class Cantonese(Chinese):
    # 间接对方法进行重写
    def land_area(self, area, rate = 0.0188):       #子类继承父类方法的操作是在def语句后接父类.方法（参数）,参数不仅可以增加,还可以修改默认值(例如area=123456,设定默认值)
        Chinese.land_area(self, area * rate)        #上面的类不管有多少个参数,引用chinese之后只能放两个.area*rate会被默认赋值到chinese类中的area
        # 直接继承父类方法，再调整参数。

gonger = Chinese()
yewen = Cantonese()
gonger.land_area(960)
yewen.land_area(960)

#----------------------------------
# 提示：初始化方法的定制，和一般的实例方法的定制是一样的。
class Chinese:
    def __init__(self, greeting='你好', place='中国'):
        self.greeting = greeting
        self.place = place

    def greet(self):
        print('%s！欢迎来到%s。' % (self.greeting, self.place))

# 请为子类完成定制，代码量：两行。
class Cantonese(Chinese):
    def __init__(self,greeting='雷猴', place='广东'):
        Chinese.__init__(self,greeting, place)
yewen = Cantonese()
yewen.greet()

