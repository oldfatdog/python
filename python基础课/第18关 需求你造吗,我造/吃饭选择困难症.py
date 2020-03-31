import random
#a = random.choice('abcdefg')  # 随机从字符串/列表/字典等对象中抽取一个元素（可能会重复）

fd_ming =['白天鹅','希尔顿','广州酒家','大龙燚']
c_ming = ['火锅','烧烤','寿司','烧鹅','牛排','小炒','甜品']

while True:
    sj_cai = random.choice(c_ming)
    print(sj_cai)
    cai_xz = input('是否选择这道菜?')
    if cai_xz == 'y':
        break

while True:
    sj_dian = random.choice(fd_ming)
    print(sj_dian)
    dian_xz = input('是否选择这家店?')
    if dian_xz == 'y':
        break

print('老铁,我们去{}这家店吃{}吧'.format(sj_dian,sj_cai))