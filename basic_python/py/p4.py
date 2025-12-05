l=eval(input("enter the value of l:"))
b=eval(input("enter the value of b:"))
num=eval(input("press 1 for area of rectangle or press any digit for perameter "))
if num==1:
    a=l*b
    print("area:",a)
else:
    p=2*(l+b)
    print("perameter:",p)
