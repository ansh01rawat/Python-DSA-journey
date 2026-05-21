class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("name:",self.name)
        print("salary:",self.salary)

E1 = Employee("Ritik", 100000)
E2 = Employee("Prarthna", 100000)

E1.display()
E2.display()