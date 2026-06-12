class Employee:
      def __init__ (self,name,emp_id,salary):
            self.name = name
            self.id = emp_id
            self.salary = salary
      def increase_salary(self,amount):
          self.salary += amount
          print("new salary =",self.salary)
      def display_info(self):
          print(self.name)
          print(self.id)
          print(self.salary)
emp1 = Employee("ansh",2323,35000)
print(emp1.salary)
emp1.increase_salary(12000)
emp1.display_info()
