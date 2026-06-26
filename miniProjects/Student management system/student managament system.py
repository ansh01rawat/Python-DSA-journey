class StudentManagementSystem:
    def __init__(self):
        self.students = {}
    def add_student(self):
        name = input("name of the student")
        try:
            enroll = int(input("enrollment no."))
        except ValueError:
            print("enroll must be an integer")
            return
        if name not in self.students:
            self.students[name] = enroll
            print(f"{name} added successfully")
        else:
            print("student already exists")
    def search_student(self):
        name = input("name of the student")
        if name in self.students:
            print(f"Name = {name} | Enrollment no. {self.students[name]}")
        else:
            print("student not found")
    def delete_student(self):
        name = input("enter name to delete")
        if name in self.students:
            del self.students[name]
            print("student deleted successfully")
        else:
            print("student not found")
    def update_student(self):
        name = input("enter name to update: ")

        if name in self.students:
            updated_name = input("enter new name: ")
            if updated_name in self.students:
                print("student with this name already exists")
                return
            self.students[updated_name] = self.students[name]
            del self.students[name]
            print("student updated successfully")
        else:
            print("student not found")
    def display_student(self):
        if not self.students:
            print("list is empty")
            return
        for name, enroll in self.students.items():
            print(f"Name = {name} | Enrollment no. {enroll}")
    def save_student(self):
        with open("students.txt", "w") as file:
            for name, enroll in self.students.items():
                file.write(f"{name},{enroll}\n")
        print("student data saved successfully")
    def load_student(self):
        try:
            with open("students.txt","r") as file:
                for line in file:
                    name,enroll = line.strip().split(",")
                    self.students[name] = int(enroll)
            print("student data loaded successfully")
        except FileNotFoundError:
            print("no previous data found")

    def menu(self):

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
                self.add_student()
            elif choice == 2:
                self.search_student()
            elif choice == 3:
                self.delete_student()
            elif choice == 4:
                self.display_student()
            elif choice == 5:
                self.update_student()
            elif choice == 6:
                print("exiting program...")
                self.save_student()
                break
            else:
                print("invalid input")
sms = StudentManagementSystem()
sms.load_student()
sms.menu()
