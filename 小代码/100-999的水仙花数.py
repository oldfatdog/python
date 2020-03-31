def shuixianhua():
    for i in range(100,1000):
        single_num = list(str(i))
        single_num_int = []

        for n in single_num:
            single_num_int.append(int(n))
        if single_num_int[0]**3 + single_num_int[1]**3 + single_num_int[2]**3 == i:
            print(i)

shuixianhua()

