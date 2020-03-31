
import math
'''
def estimated(size=1,number=None,time=None):
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))  
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))  

choice = input('请选择计算类型：（1-人力计算，2-工时计算）')
if choice == '2':
    size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
    number = int(input('请输入人力数量：（请输入整数）'))
    time = None
    estimated(size,number,time)
elif choice == '1':
    size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
    number = None
    time = float(input('请输入工时数量：（可以输入小数）'))
    estimated(size,number,time)'''
#-----------多函数改造------------------------
def estimated(data):
    size=data[0]
    number=data[1]
    time=data[2]
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))  
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))  

def choose():
    choice = input('请选择计算类型：（1-人力计算，2-工时计算）')
    if choice == '2':
        size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
        number = int(input('请输入人力数量：（请输入整数）'))
        time = None
        return size,number,time
    elif choice == '1':
        size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
        number = None
        time = float(input('请输入工时数量：（可以输入小数）'))
        return size,number,time
def cost():
    estimated(choose())

def again():
    while True:
        cost()
        a=input('是否结束?\n1-结束\n2-继续') 
        if a =='1':
            break
again()
'''
#---------------global全局使得超越函数套-------------
k=1
def again():
    # 声明全局变量key，以便修改该变量
    global key
    a = input('是否继续计算？继续请输入y，输入其他键将结束程序。')
    if a != 'y':
        # 如果用户不输入'y'，则把key赋值为0
        key = 0  

# 主函数
def main():
    print('欢迎使用工作量计算小程序！')
    while key == 1:
        my_input = myinput()
        estimated(my_input)
        again()
    print('感谢使用工作量计算小程序！')'''