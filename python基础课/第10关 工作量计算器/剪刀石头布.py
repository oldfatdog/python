import random

# 出拳
punches = ['石头','剪刀','布']
computer_choice = random.choice(punches)    #random.choice():从中随机选择(选择之前肯定先遍历列表,所以可以用上索引index)
user_choice = ''
user_choice = input('请出拳：（石头、剪刀、布）')  # 请用户输入选择
while user_choice not in punches:  # 当用户输入错误，提示错误，重新输入
    print('输入有误，请重新出拳')
    user_choice = input()

# 亮拳
print('————战斗过程————')
print('电脑出了：%s' % computer_choice)
print('你出了：%s' % user_choice)

# 胜负
print('—————结果—————')
if user_choice==computer_choice:
    print('同归于尽')
else:
    if user_choice=='石头':
        if user_choice == '石头' and computer_choice == '剪刀' :
            print('你胜利了')
        else :
            print('你输了')
    elif user_choice=='剪刀':
        if user_choice=='剪刀' and computer_choice == '布' :
            print('你胜利了')
        else :
            print('你输了')
    else :
        if user_choice=='布' and computer_choice == '石头' :
            print('你胜利了')
        else :
            print('你输了')
        	
#------------另外一种写法-----------(注意判定输赢处)-----------------

# 出拳
punches = ['石头','剪刀','布']
computer_choice = random.choice(punches)
user_choice = ''
user_choice = input('请出拳：（石头、剪刀、布）')  # 请用户输入选择
while user_choice not in punches:  # 当用户输入错误，提示错误，重新输入
    print('输入有误，请重新出拳')
    user_choice = input()

# 亮拳
print('————战斗过程————')
print('电脑出了：%s' %(computer_choice))
print('你出了：%s' %(user_choice))

# 胜负
print('—————结果—————')
if user_choice == computer_choice:  # 使用if进行条件判断
    print('平局！')
# 请你将下一行代码用 index()函数 实现（不再有 and 和 or），从而简化代码。
elif (user_choice,computer_choice) in [('石头','剪刀'),('剪刀','布'),('布','石头')]:
    #进一步简化: punches.index(computer_choice) 即从 punches 列表中索引 computer_choice 遍历过的元素,得到遍历时元素对应的顺序,即石头-0,剪刀-1,布-2
    #玩家的选择也时从 punches 中选择的,所以也能用 punches[]来表示,如果玩家 punches[] 的序列刚好比 computer_choice -1.则玩家就会赢,如下列代码
    # user_choice == punches[punches.index(computer_choice)-1]: 
    print('你赢了！')
else:
    print('你输了！')
    
