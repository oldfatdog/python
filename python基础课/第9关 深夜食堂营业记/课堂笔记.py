#定义函数
#def    函数名(参数):
#       函数体
#       retur 语句

#-------------------------------

#函数名：1. 名字最好能体现函数的功能，一般用小写字母和单下划线、数字等组合
#      2. 不可与内置函数重名（内置函数不需要定义即可直接使用）
# def math(x):
# 参数：根据函数功能，括号里可以有多个参数，也可以不带参数，命名规则与函数名相同
# 规范：括号是英文括号，后面的冒号不能丢
#    y = 3x + 5
# 函数体：函数的执行过程，体现函数功能的语句，要缩进，一般是四个空格
#    return y
# return语句：后面可以接多种数据类型，如果函数不需要返回值的话，可以省略

#---------定义函数y=3x+5---------

def hanshu(x):
    y=3*x+5
    return y

print(hanshu(2))

#----------定义函数y=x^2 + x------

def pingfang(x):
    y=x**2 + x
    return y
print(pingfang(11))

#------------自写len()函数----------
'''
def my_len(words):
    counter = 0
    for i in words:
        counter = counter + 1
    return counter

a = '三根皮带，四斤大豆'
print(my_len(a))'''

#--------------函数进阶使用---------------

import random 
appetizer = ['话梅花生','拍黄瓜','凉拌三丝']
def coupon(money):
    if money < 5:
        a = random.choice(appetizer)
        return a
    elif 5 < money < 10:
        b = random.choice (appetizer)
        return b, '溏心蛋'

result = coupon(6)
print(result[0],result[1])
# result是一个元组

#-------------计算本月增长率--------------

#num1 本月利润
#num2 上个月利润
def div(num1, num2):
    growth = (num1 - num2) / num2
    percent = str(growth * 100) + '%'
    return percent

def warning():
    print('Error: 你确定上个月一毛钱都不赚不亏吗？')

def main():
    while True:
        num1 = float(input('请输入本月所获利润'))
        num2 = float(input('请输入上月所获利润'))
        if num2 == 0:
            warning()
            continue
        else:
            print('本月的利润增长率：' + div(num1,num2))
            break

main()