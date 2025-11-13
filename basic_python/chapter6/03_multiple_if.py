age=int(input("enter your age="))
if(age%2==0):
    print("age is evan number")
if(age>=18):
    print("eligible for vote")
    print("good morning sir!")
elif(age==0):
    print("you enter zero")
    print("and zero is not a valid age")
elif(age<0):   
    print("you enter negtive number on youe age")
    print("plese corect it")
elif(age<=18):
    print("you not eligible for vote")
print("end of the program")
