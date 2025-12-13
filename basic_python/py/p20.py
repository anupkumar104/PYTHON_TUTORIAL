import numpy as np
x= np.array([[1,2,3],[3,4,5],[5,6,7]])
sum=0
for i in x:
    for j in x:
        if i==j:
            sum=sum+x[i][j]
print("sum:",sum)