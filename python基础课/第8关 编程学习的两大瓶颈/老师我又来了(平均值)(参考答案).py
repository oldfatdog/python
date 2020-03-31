import numpy as np

scores1 =  [91, 95, 97, 99, 92, 93, 96, 98]  

scores2 = []

average = np.mean(scores1)  # np.mean():求列别平均值
print('平均成绩是：{}'.format(average))

for score in scores1:
    if score < average:
        scores2.append(score)
        continue  # 少于平均分的成绩放到新建的空列表中，然后继续判断。
print(' 低于平均成绩的有：{}'.format(scores2))  # 上个关卡选做题的知识。

# 下面展示一种NumPy数组的操作，感兴趣的同学可以自行去学习哈。
scores3 = np.array(scores1)     #np.array():使得列表使得列别项加上true false属性
print(' 低于平均成绩的有：{}'.format(scores3[scores3<average]))     #符合不等式的项显示为ture并可以直接读取    
