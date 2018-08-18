# Instance variable: Datas are unique for each instance
# Class variable: variables(Datas) that are shared among all instances of a class
# Class method is declared by adding a decorator and uses a cls argument -> Usually to create an instance
# Static method doesn't have cls and self as arguments
class Employee:
    raiseAmount = 1.04 # class var
    numOfEmployees = 0

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName # instance var
        self.lastName = lastName # instance var
        self.salary = salary # instance var
        self.email = f'{firstName}.{lastName}@email.com'
        Employee.numOfEmployees += 1 # class var

    def printFullName(self):
        return (f'{self.firstName} {self.lastName}')

    def raiseSalary(self):
        self.salary = int(self.salary * Employee.raiseAmount)

  
    @classmethod
    def setRaiseAmount(cls, amount):
        cls.raiseAmount = amount
 
    @classmethod
    def fromStringCreateEmployee(cls, string):
        first, last, pay = string.split('-')  
        return cls(first, last, pay) 

    @staticmethod
    def isWorkday(day):
        if day.weekday() == 6 or day.weekday() == 7:
            return False
        return True

class Developer(Employee):
    raiseAmount = 1.10
    def __init__(self, firstName, lastName, salary, progLanguage):
        super().__init__(firstName, lastName, salary) # calling parent's constructor
        self.progLanguage = progLanguage
    pass

class Manager(Employee):
    raiseAmount = 1.15
    def __init__(self, firstName, lastName, salary, employees=None):
        super().__init__(firstName, lastName, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addEmployee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def removeEmployee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def printAllEmployees(self):
        for employee in self.employees:
           print('-->', employee.printFullName())   

manager1 = Manager('Nathaniel', 'Lee', 150000)
emp1 = Developer('Binh', 'Vo', 65000, 'Python')
emp2 = Employee('Trash', 'Bin', 40000)
manager1.addEmployee(emp1)
manager1.addEmployee(emp2)
print(manager1.email)
manager1.printAllEmployees()

# isinstance(), issubclass() - return a bool if a an instance is part of a particular class or subclass
print(isinstance(emp1, Employee))
print(issubclass(manager1, Employee))
print(issubclass(Manager, Developer))






emp_str_3 = 'David-Lee-90000'
emp3 = Employee.fromStringCreateEmployee(emp_str_3)
print(emp3.__dict__)
# print(help(Developer))
Employee.setRaiseAmount(1.05)

# Both ways are ==, Using an instance to call a method
# Using a Class and pass in the instance for it to reference it-'self'
print(emp1.printFullName())  
print(Employee.printFullName(emp1))
print(emp2.__dict__) # Getting all attributes of an instance or a class

import datetime
day_off = datetime.date(2018, 8, 17)
print(Employee.isWorkday(day_off))
