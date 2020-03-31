# 先补全代码，然后再运行。
# 可体会多重继承中的就近原则。
class Teacher:
    face = 'serious'
    job = 'teacher'

class Father:
    face = 'sweet'
    parenthood = 'dad'

class time1(Teacher,Father):
    face = 'gentel'

class time2(Teacher,Father):
    pass

time3=time1()
time4=time2()
print(time3.face)
print(time4.face)