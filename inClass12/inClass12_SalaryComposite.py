from inClass12_Salary import *

# 7.2 – Create a worker class: (for composition type)
class Worker1:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.salary_obj = Salary(pay, bonus)  # composition created a salary object during __init__()

    # calculates the total salary with the help of annual_salary() method declared in the Salary class
    def total_sal(self):
        return self.salary_obj.annual_salary()

    def __str__(self):
        return f'employee: {self.name}, age: {self.age}, annual_salary: {self.total_sal()}'


# Making an object of the class Employee1
# and providing necessary arguments
pay = 10000
bonus = 1500

emp = Worker1('Mary', 25, pay, bonus)
print('composition mode: ', emp)


"""
Results:
composition mode:  employee: Mary, age: 25, annual_salary: 121500
"""