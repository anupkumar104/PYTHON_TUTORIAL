#given number the is krishnasmurti number  or not
num=int(input("enter a number:"))
add=0
temp=num
while temp!=0:
    digit=temp%10
    fact=1
    for i in range(1,digit+1):
        fact= fact*i
    add= add+fact
    temp =temp//10

if add==num:
    print("number is krishnamurti")
else:
    print("number is not krishnamurti")