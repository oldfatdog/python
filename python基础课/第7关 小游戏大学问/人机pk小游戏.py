import random,time
playerwin=0
pcwin=0
while True:
    for i in range(1,4):
        print('现在是第'+str(i)+'局')
        time.sleep(1)
        player_blood=random.randint(100,150)
        player_attack=random.randint(30,50)
        print('[玩家] \n 血量: %s \n攻击力: %s' % (player_blood,player_attack))
        time.sleep(1)
        print('-----------------')
        time.sleep(1)

        pc_blood=random.randint(100,150)
        pc_attack=random.randint(30,50)
        print('[敌人] \n血量:%s \n攻击力:%s' % (pc_blood,pc_attack))
        time.sleep(1)
        print('-----------------')
        time.sleep(1)

        while (player_blood > 0) and (pc_blood > 0):
            player_blood = player_blood - pc_attack
            pc_blood = pc_blood - player_attack
            print('你发起了攻击,玩家剩余血量%s' % player_blood)
            time.sleep(1)
            print('敌人向你发起了攻击,敌人剩余血量 %s' % pc_blood)
            time.sleep(1)
            print('-----------------')
            time.sleep(1)
            
        if player_blood >0 and pc_blood<=0:
            print('你胜利了')
            time.sleep(1)
            playerwin += 1
        elif player_blood <=0 and pc_blood>0:
            print('悲催,敌人把你干掉了')
            time.sleep(1)
            pcwin += 1
        else:
            print('同归于尽')

        if playerwin > pcwin:
            print('[最终结果:你胜利了!]')
        elif playerwin < pcwin :
            print('[最终结果:你输了!]')
        else:
            print('平局')
    if '是' != input('是否再来一盘?'):
        break
'''`
while True:
    a1 = input('要继续游戏吗，请输入n退出，输入其他继续：')
    if a1 == 'n':
        break

# 方案2
again = True
while again:
    a2 = input('要继续游戏吗，请输入y继续，输入其他退出：')
    if a2 == 'y':
        again = True
    else:
        again = False'''