scores =  [91, 95, 97, 99, 92, 93, 96, 98]  
c=0
low=[]
import numpy as np  # 导入 numpy库，下面出现的 np 即 numpy库

for i in scores:
    c=i+c
avg=c/len(scores)
print(avg)
for j in scores:
    if j < avg:
        low.append(j)
print(low)

