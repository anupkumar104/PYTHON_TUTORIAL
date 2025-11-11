#Write a program to accept marks of 6 students and display them in a sorted 
# manner
student=[]
s1=input("enter the student name 1:")
student.append(s1)
s2=input("enter the student name 2:")
student.append(s2)
s3=input("enter the student name 3:")
student.append(s3)
s4=input("enter the fruit name 4:")
student.append(s4)
s5=input("enter the student name 5:")
student.append(s5)
s6=input("enter(s5) the student name 6:")
student.append(s6)
student.sort()
print(student)