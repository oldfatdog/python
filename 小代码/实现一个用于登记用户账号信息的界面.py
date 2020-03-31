import easygui as eg

user_list = []

while 1:
    fieldNames = ['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
    fieldValues = []

    info_list = ['用户名','真实姓名','固定电话','手机号码','QQ','E-mail']
    info_dict = {}

    msg = '带[*]为必填信息'
    title = '账号中心'
    fieldValues = eg.multenterbox(msg,title,fieldNames)
    if fieldValues == None:
        break
    if (fieldValues[0] or fieldValues[1] or fieldValues[3] or fieldValues[5]) == (' ' or None):
        print('重新输入')
        continue
    for each in range(len(fieldValues)):
        info_dict[info_list[each]] = fieldValues[each]
    
    user_list.append(info_dict)
    
    if eg.ccbox():
        pass         # 用户选择继续
    else:
        print(user_list)
        break      # 用户选择取消


