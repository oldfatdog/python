# try...except...
# 尝试执行try后面的代码,如果报错就执行except后面的代码
# 用于对异常输入的处理

#---------------------------
# （1）因为不知道用户什么时候才会输入正确，所以设置while循环来接受输入，只要用户输入不是数字就会一直循环，输入了数字就break跳出循环。
# （2）使用try……except……语句，当用户输错的时候会给予提示。
while True:
    try:
        age = int(input('你今年几岁了？'))
        break
    except ValueError:
        print('你输入的不是数字！')

if age < 18:
    print('不可以喝酒噢')

#-----------再一个例子--------
num = [1,2,0,3]
for x in num:
    try:
    #尝试执行下列代码
        print (6/x)
        #使用6除以num中的元素，并打印
    except ZeroDivisionError:
    #除非发生ZeroDivisionError报错，执行下列代码：
        print('0是不能做除数的！')
        #打印“0是不能做除数的！”