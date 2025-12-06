a=eval(input("enter the value of a:"))
b=eval(input("enter the value of b:"))
c=eval(input("enter the value of c:"))
d=eval(input("enter the value of d:"))
if a<b and a<c and a<d:
    print("a is samll")
elif b<c and b<d:
    print("b is samll")
elif c<d :
    print("c is small")
else:
    print("d is small")