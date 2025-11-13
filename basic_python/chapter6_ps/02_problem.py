# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.
mark1=int(input("enter your marks in subject 1="))
mark2=int(input("enter your marks in subject 2="))
mark3=int(input("enter your marks in subject 3="))
per=(mark1+mark2+mark3)/3
if(per>=40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("you pass",per)
else:
    print("you fail",per)