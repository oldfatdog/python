students = ['小明','小红','小刚']
for i in range(3):
    print(students)
    student0=students[0]
    student1=students[1]
    student2=students[2]
    students[0]=student1
    students[1]=student2
    students[2]=student0


n = 0
while n < 3:
    print(students)
    n=n+1
    student0=students[0]
    student1=students[1]
    student2=students[2]
    students[0]=student1
    students[1]=student2
    students[2]=student0


for i in range(3):
    print(students)
    students.append(students.pop(0))
