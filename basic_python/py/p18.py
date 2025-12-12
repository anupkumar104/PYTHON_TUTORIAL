import numpy as np
arr=np.array([12, 43, 44, 65, 22, 11, 55, 1, 10, 27])
print("Elements of Array: ",arr)
length=len (arr)
big =small= arr[0] 
for i in range (length):
    if arr[i]>big:
     big=arr[i]
     pos1= i
    elif arr[i]<small:
        small=arr[i]
        pos2=i

print("Highest element: ", big, "Position : ",pos1)

print("Lowest element: ", small, "Position : ",pos2)