# 定制计时器
import time

class MYtimer:
# 定义初始变量
    def __init__(self):
        self.unit = ['年','月','日','小时','分钟','秒']
        self.prompt = '开始计时'
        self.lasted = []
        self.start_time = 0
# 自动输出
    def __str__(self):
        return self.prompt

# 定义加法
    def __add__(self,other):
        prompt = '总共运行了'
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt
# 开始计时
    def start(self):
        self.start_time = time.localtime()
        self.prompt = '提示:先调用stop()停止计时'
        print('计时开始了')
# 停止计时
    def stop(self):
        if not self.start_time:
            print('请先调用start()进行计时')
        else:
            self.stop_time = time.localtime()
            self._calc()
            print('计时结束')
# 内部方法,计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            self.lasted.append(self.stop_time[index] - self.start_time[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        # 为下一轮计时初始化变量
        self.start_time = 0
        self.stop_time = 0
a = MYtimer()
a.start()
time.sleep(4)
a.stop()
print(a)