import easygui as eg
import random

times = 3
secret = random.randint(1,10)
eg.msgbox('------------------我爱鱼C工作室------------------')
# 这里先给guess赋值（赋一个绝对不等于secret的值）
guess = 0

# print()默认是打印完字符串会自动添加一个换行符，end=" "参数告诉print()用空格代替换行
# 嗯，小甲鱼觉得富有创意的你应该会尝试用 end="JJ"？
eg.msgbox("不妨猜一下小甲鱼现在心里想的是哪个数字：")
while (guess != secret) and (times > 0):
    temp = eg.integerbox(lowerbound=1, upperbound=10)
    guess = int(temp)
    times = times - 1 # 用户每输入一次，可用机会就-1
    if guess == secret:
        eg.msgbox("我草，你是小甲鱼心里的蛔虫吗？！")
        eg.msgbox("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            eg.msgbox("哥，大了大了~~~")
        else:
            eg.msgbox("嘿，小了，小了~~~")
        if times > 0:
            eg.msgbox("再试一次吧：")
        else:
            eg.msgbox("机会用光咯T_T")
eg.msgbox("游戏结束，不玩啦^_^")