# EX7. Aggregation / Composition (“has a”): There are two kinds of composition: “has-a” and “own-a

from inClass12_Salary import *
# Code to demonstrate aggregation

# Employee1 class with public method total_sal()

# 7.3 – create a worker class (for Aggregation type):


class Worker1:
    def __init__(self, name, age, sal):
        self.name = name
        self.age = age

        # initializing the sal parameter

        self.agg_salary = sal  # Aggregation, sal is a salary object

    # calculates the total salary with the help of annual_salary() method declared in the Salary class
    def total_sal(self):
        return self.agg_salary.annual_salary()

    def __str__(self):
        return f'employee: {self.name}, age: {self.age}, annual_salary: {self.total_sal()}'


# creating the salary class object with the required parameters
pay = 10000
bonus = 1500
salary = Salary(pay, bonus)

emp = Worker1('John', 25, salary)
print('aggregation mode: ', emp)

"""
Results:
aggregation mode:  employee: John, age: 25, annual_salary: 121500
"""