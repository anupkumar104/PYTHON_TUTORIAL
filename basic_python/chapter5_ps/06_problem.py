# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.
f={

}
name=input("enter your name:")
lan=input("enter your language:")
f.update({name:lan})
name=input("enter your name:")
lan=input("enter your language:")
f.update({name:lan})
name=input("enter your name:")
lan=input("enter your language:")
f.update({name:lan})
name=input("enter your name:")
lan=input("enter your language:")
f.update({name:lan})
print(f)
