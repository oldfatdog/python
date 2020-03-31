import time
import random

while True:

    playerwin = 0
    enemywin = 0

    for i in range(1,4):

        time.sleep(2)
        print('现在是第 %s 局' % i)

        player_blood = random.randint(100,150)
        player_attack = random.randint(30,50)
        enemy_blood = random.randint(100,150)
        enemy_attack = random.randint(30,50)

        print('player \nlife: %s \nacttck: %s'%(player_blood,enemy_attack))
        print('-------------------------')
        time.sleep(1)
        print('enemy \nlife: %s \nacttck: %s'%(enemy_blood,enemy_attack))
        print('-------------------------')

        while player_blood >= 0 and enemy_blood >= 0:
            player_blood = player_blood - enemy_attack
            enemy_blood = enemy_blood - player_attack
            print('玩家发起了攻击 \n敌人剩余血量：%s'%enemy_blood)
            print('敌人向玩家发起了攻击 \n玩家剩余血量：%s'%player_blood)
            print('------------------------')
            time.sleep(1.5)

        if player_blood > 0 and enemy_blood <=0:
            print('u win')
            playerwin = playerwin + 1
        elif player_blood <= 0 and enemy_blood > 0:
            print('enemy win')
            enemywin = enemywin + 1
        else:
            print('both dead')

    if playerwin > enemywin:
        print('player win')
    elif playerwin < enemywin:
        print('enemy win')
    else:
        print('平局')

    choice = int(input('是否再玩一局？1是2否'))
    if choice == 1:
        pass
    elif choice == 2:
        break
    else:
        print('就当你不想玩了')
        break