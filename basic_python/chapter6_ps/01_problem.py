#  Write a program to find the greatest of four numbers entered by the user
num1=int(input("enter the number1="))
num2=int(input("enter the number2="))
num3=int(input("enter the number3="))
num4=int(input("enter the number4="))
if(num1>num2 and num1>num3 and num1>num4):
    print("number 1 is gretest number than all number")
elif(num2>num1 and num2>num3 and num2>num4):
    print("number 2 is gretest number than all number")
elif(num3>num2 and num3>num1 and num3>num4):
    print("number 3 is gretest number than all number")
elif(num4>num1 and num4>num2 and num4>num3):
    print("number 4 is gretest number than all number")
