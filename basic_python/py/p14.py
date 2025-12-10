list1 = []

def show_list():
    print("Current List:", list1)

def create_list():
    global list1
    size = int(input("Enter the number of elements: "))
    list1 = []
    for i in range(size):
        val = int(input(f"Enter element {i+1}: "))
        list1.append(val)
    print("List created successfully.")
def delete():
    if not list1:
        print("the list is empty")
    else:
        val=int(input("enter the value  for delete"))
        if val in list1:
            list1.pop(val)
            print("the value is deleted from list")
        else:
            print("the value is not found in the list")
def insert():
    val = int(input("enter the number to insert in the list"))
    ind= int(input("enter the index"))
    list1.insert(val,ind)
    print("the vale is inserted")
def max1():
    if not list1:
        print("empty list")
    else:
        m=max(list1)
        print("the max vale is",m)
def min1():
    if not list1:
        print("empty list")
    else:
        m=min(list1)
        print("the min vale is",m)