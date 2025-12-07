#given number the is krishnasmurti number  or not
# write a program to print fibonacci series
num=eval(input("enter a number:"))
n1=0
n2=1
for i in range(num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)
