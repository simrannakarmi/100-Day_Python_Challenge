import pickle

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone No.: ")
    data = [name, phone]
    f = open("contacts.dat", "ab") #ab = append binary
    pickle.dump(data, f)
    f.close()
    print("Contact added successfully")
    
def display():
    f = open("contacts.dat", "rb")
    print("-" * 30)
    print("Name\t\tContact")
    try:
        while True:
            data = pickle.load(f)
            print(data[0]+"\t\t"+data[1])
    except:
        f.close()
        

while True:
    print("-" * 30)
    print("Press 1 - Add a New Contact")
    print("Press 2 - Display All Contact")
    print("Press 3 - Search a Contact")
    print("Press 4 - Update a Contact")
    print("Press 5 - Delete a Contact")
    print("Press any other number to EXIT")
    print("-" * 30)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_contact()
    elif choice == 2:
        display()
    elif choice == 3:
        search()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    else:
        break