import easygui as eg

user_list = []

while 1:
    fieldNames = ['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
    fieldValues = []
    door = 1
    info_list = ['用户名','真实姓名','固定电话','手机号码','QQ','E-mail']
    info_dict = {}

    msg = '带[*]为必填信息'
    title = '账号中心'

    fieldValues = eg.multenterbox(msg,title,fieldNames)
    if fieldValues == None:
        break

    for each in range(len(fieldValues)):
        if fieldValues[each].strip() =='' and fieldNames[each][0] == '*':
            door = 0
            break
    if door == 0:
        break
    for each in range(len(fieldValues)):
        info_dict[info_list[each]] = fieldValues[each]
    
    user_list.append(info_dict)
    
    if eg.ccbox():
        pass         # 用户选择继续
    else:
        print(user_list)
        break      # 用户选择取消
