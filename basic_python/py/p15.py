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
        print("The list is empty")
    else:
        val = int(input("Enter the value to delete: "))
        if val in list1:
            list1.remove(val)   
            print("The value is deleted from the list")
        else:
            print("The value is not found in the list")

def insert():
    val = int(input("Enter the number to insert in the list: "))
    ind = int(input("Enter the index: "))
    if 0 <= ind <= len(list1):
        list1.insert(ind, val)  
        print("The value is inserted")
    else:
        print("Invalid index")

def max1():
    if not list1:
        print("Empty list")
    else:
        print("The max value is", max(list1))

def min1():
    if not list1:
        print("Empty list")
    else:
        print("The min value is", min(list1))
def menu():
    while True:
        print("\n------ Menu ------")
        print("1. Create List")
        print("2. Show List")
        print("3. Insert Element")
        print("4. Delete Element")
        print("5. Find Max")
        print("6. Find Min")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_list()
        elif choice == 2:
            show_list()
        elif choice == 3:
            insert()
        elif choice == 4:
            delete()
        elif choice == 5:
            max1()
        elif choice == 6:
            min1()
        elif choice == 7:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
