# 请你改造下面的代码，目标：不论输入了什么，程序都不会因报错而停止（即找到所有的报错类型）。

while True:
    print('\n欢迎使用除法计算器！\n')

    x = input('请你输入被除数：')
    y = input('请你输入除数：')
    try:
        z = float(x)/float(y)
    # 下面是 print函数的一种用法，用逗号隔开，可在同一行打印不同类型的数据。
        print(x,'/',y,'=',z)
        break  # 当成功运行一次除法运算后，退出程序。
    except ZeroDivisionError:
        print('除数不能为零哦')
    except ValueError:
        print('要输入整数或者小数哦')
        
 # 方式2：将两个（或多个）异常放在一起，只要触发其中一个，就执行所包含的代码。
    # except(ZeroDivisionError,ValueError):
    #     print('你的输入有误，请重新输入！')
    
    # 方式3：常规错误的基类，假设不想提供很精细的提示，可以用这个语句响应常规错误。
    # except Exception:
    #     print('你的输入有误，请重新输入！')
    