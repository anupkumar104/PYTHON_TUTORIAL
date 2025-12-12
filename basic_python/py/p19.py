#to find the index of  search element in array
import numpy as np
arr=np.array([12, 43, 44, 65, 22, 11, 55, 1, 10, 27])
print("Elements of Array: ",arr)
a=int(input("enter the element:"))
length=len (arr)
for i in range (length):
    if arr[i]==a:
        pos=i
print("number is :",a,"position:",pos)   