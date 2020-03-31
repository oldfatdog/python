# 新建一个方法，让实例只要调用一个方法，就能打印出两个信息。
# 代码完成后，请运行一下，验证是否成功。
class Chinese:

    def __init__(self,hometown,region):
        self.hometown = hometown
        self.region = region
        print('程序持续更新中……')

    def born(self):
        print('我生在%s。'%(self.hometown))
    def live(self):
        print('我在%s。'%(self.region))

    def info(self):
        self.born()     #调用类内部函数
        self.live()
kik=Chinese('韶关','广州')
kik.info()