# Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50=> F
m=int(input("enter your total number="))
if(m>100):
    print("you entered more then 100....plese correct it.....")
else:
    if(m>=90 and m<=100):
        print("ex grade")
    elif(m>=80 and m<=90):
        print("a grade")
    elif(m>=70 and m<=80):
        print("b grade")
    elif(m>=60 and m<=70):
        print("c grade")
    elif(m>=50 and m<=60):
        print("d grade")
    elif(m<50):
        print("f grade")
        print("try next time")