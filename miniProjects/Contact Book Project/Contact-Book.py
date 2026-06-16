contacts = {}

def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")

    contacts[name] = number

    print("Contact added successfully")

def search_contact():
    name = input("Enter name: ")

    if name in contacts:
        print("phone number", contacts[name])

    else:
        print("contact not found")

def delete_contact():
    name = input("Enter name: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully")
    else:
        print("contact not found")

def display_contacts():
    if len(contacts) == 0:
        print("No contacts found")

    else:
        print("Contact list:")
        for name,number in contacts.items():
            print(name, " : ", number)

while True:

    print("Welcome to the contact book")
    print("1 -> add contact")
    print("2 -> search contact")
    print("3 -> delete contact")
    print("4 -> display contacts")
    print("5 -> exit")

    enter_choice = input("Enter choice: ")
    if enter_choice == "1":
        add_contact()
    elif enter_choice == "2":
        search_contact()
    elif enter_choice == "3":
        delete_contact()
    elif enter_choice == "4":
        display_contacts()
    elif enter_choice == "5":
        print("exiting program...")
        break
    else:
        print("invalid choice")


