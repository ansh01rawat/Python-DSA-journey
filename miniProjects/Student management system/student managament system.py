students = {}
def add_student():
    name = input("name of the student")
    try:
       enroll = int(input("enrollment no."))
    except ValueError:
        print("enroll must be an integer")
        return
    if name not in students:
        students[name] = enroll
        print(f"{name} added successfully")
    else:
        print("student already exists")
def search_student():
    name = input("name of the student")
    if name in students:
        print(f"Name = {name} | Enrollment no. {students[name]}")
    else:
        print("student not found")
def del_student():
    name = input("enter name to delete")
    if name in students:
        del students[name]
        print("student deleted successfully")
    else:
        print("student not found")
def update_student():
    name = input("enter name to update: ")

    if name in students:
        updated_name = input("enter new name: ")
        if updated_name in students:
            print("student with this name already exists")
            return
        students[updated_name] = students[name]
        del students[name]
        print("student updated successfully")
    else:
        print("student not found")


def display_students():
    if not students:
        print("list is empty")
        return
    for name,enroll in students.items():
        print(f"Name = {name} | Enrollment no. {enroll}")


def menu():

    while True:
        print("\n======Student Management System======")

        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Display Student")
        print("5. Update Student")
        print("6. Exit Program")
        try:
            choice = int(input("enter your choice "))
        except ValueError:
            print("please enter a valid choice")
            continue
        if choice == 1:
            add_student()
        elif choice == 2:
            search_student()
        elif choice == 3:
            del_student()
        elif choice == 4:
            display_students()
        elif choice == 5:
            update_student()
        elif choice == 6:
            print("exiting program...")
            break
        else:
            print("invalid input")


menu()
