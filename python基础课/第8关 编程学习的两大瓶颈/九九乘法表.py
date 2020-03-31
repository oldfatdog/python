for i in range(1,10):
    for o in range(1,10):
        print('%d X %d = %d' % (o,i,i*o),end=' ')  #end='' 使接下来的输出不换行
        if i==o:
            print('')     #手动换行
            break


for j in range(1,10):
    for k in range(1,j+1):
        #print(str(k)+' x '+str(j)+' = '+str(k*j),end=' ')
        print('%s x %s = %s' %(k,j,j*k),end=' ')
    print('')

'''
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d X %d = %d' % (j,i,i*j),end = '  ') 
        j += 1
    print('')
    i += 1
'''


  