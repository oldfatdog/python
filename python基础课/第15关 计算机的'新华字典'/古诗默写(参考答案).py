list_test = ['一弦一柱思华年。\n','只是当时已惘然。\n']  # 将要默写的诗句放在列表里。
with open ('poem2.txt','r') as f:
    lines = f.readlines()
print(lines)
with open('poem2.txt','w') as new:
    for line in lines:
        if line in list_test:  # 属于默写列表中的句子，将其替换成横线。
            new.write('____________。\n')
        else:
            new.write(line)


# ======================================================
# 参考答案不够好,下面的更给力

def replace_word():
    replace_world=input('想替换啥')
    replaced_world=input('想替换成啥')

    with open('poem2.txt','r',encoding='utf-8') as f:
        content = f.readlines()

    with open('poem2.txt','w',encoding='utf-8') as g:
        for i in range(len(content)):
            data_bridge1 = content[i]
            if replace_world in content[i]:
                data_bridge=data_bridge1.replace(replace_world,replaced_world)
                g.write(data_bridge)
            else:
                g.write(data_bridge1)

# ==================================================