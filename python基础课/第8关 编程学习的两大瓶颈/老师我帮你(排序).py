a=[95, 91, 97, 99]
b=[92, 93, 96, 98] 
c=a+b

'''
for l in range(len(c)-1):   #重复以下过程
    for i in range(len(c)-1):   #将i项与i+1项做对比,如果i>i+1项,值互换
        if c[i]>c[i+1]:     
            j=c[i+1]    
            c[i+1]=c[i]
            c[i]=j
    print(c)
'''
c.sort()    # sort()函数使用后列表会改变
print(c)

d=sorted(c)     #sorted()使用后需赋值使用
print(d)

c.reverse()     #反序
print(c)