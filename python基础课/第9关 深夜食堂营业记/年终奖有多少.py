def salary(time):
    i=int(time)
    if i < 6:
        money=str(500)+'元'
    elif 12 >= i >= 6:
        money=str(120*i)+'元'
    else:
        money=str(180*i)+'元'
    return money

def result():
    i=input('请输入员工姓名')
    j=input('请输入工作时长')
    k=salary(j)
    return print('{}该员工来了{}个月,获得奖金{}'.format(i,j,k))
result()

#----------参考答案-------------------
def cash(i):
    if i < 6:
        money=str(500)+'元'
    elif 12 >= i >= 6:
        money=str(120*i)+'元'
    else:
        money=str(180*i)+'元'
    return money

def info(name,month):
    bonus=cash(month)
    print('{}该员工来了{}个月,获得奖金{}'.format(name,month,bonus))
info('大黄',5424)