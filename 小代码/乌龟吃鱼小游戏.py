import random

class Animal:
    def start_coordinate(self):
        x = random.randint(1,10)
        y = random.randint(1,10)
        return [x,y]

    def move(self,mode=1):
        self.mode = mode
        if self.mode == 1:
            m = random.choice([-1,0,1])
            n = random.choice([-1,0,1])
        elif self.mode == 2:
            m = random.choice([-2,-1,0,1,2])
            n = random.choice([-2,-1,0,1,2])
        else:
            print('move parameter only by 1(fish) or 2(tutle)')
            raise ValueError
        return [m,n]
tutle = Animal()
fish = Animal()

tutle_coordinate = tutle.start_coordinate()
# [6, 7] [3, 8]

# 储存10条鱼的列表
fish_pool = []
# 创建10条鱼
for i in range(10):
    fish_pool.append(fish.start_coordinate())
print(fish_pool)

tutle_power = 100
power_award = 20

while tutle_power:
    
    # 乌龟的移动
    tutle_move = tutle.move(2)
    i = tutle_coordinate[0] + tutle_move[0]
    if i not in range(1,11):
        i = tutle_coordinate[0] - tutle_move[0]
    j = tutle_coordinate[1] + tutle_move[1]
    if j not in range(1,11):
        j = tutle_coordinate[1] - tutle_move[1]
    tutle_movement = [i,j] #乌龟移动后的位置
    # 鱼们的移动
    for fl in range(len(fish_pool)):
        fish_move = fish.move()
        m = fish_pool[fl][0]+fish_move[0]
        if m not in range(1,11):
            m = fish_pool[fl][0] - fish_move[0]
        n = fish_pool[fl][1]+fish_move[1]
        if n not in range(1,11):
            n = fish_pool[fl][1] - fish_move[1]
        fish_pool[fl] = [m,n] #鱼们移动后的位置

    print('乌龟的位置移动到了%s'%tutle_movement)
    print('鱼的位置移动到了%s'%fish_pool)

    for fc in fish_pool:
        if tutle_movement == fc:
            fish_pool.remove(fc)
            print('乌龟吃掉了一条鱼,获得体力20点')
            tutle_power = tutle_power + power_award

    print('现在池子里还有%s条鱼'%len(fish_pool))
    if fish_pool == []:
        print('池子里的鱼被吃光了,乌龟吃饱了,游戏结束')
        break
    else:
        tutle_power = tutle_power - 1
        print('乌龟到处爬,消耗1点体力,现在还有%s点体力'%tutle_power)
        if tutle_power == 0:
            print('乌龟没有体力啦,游戏结束')
            break