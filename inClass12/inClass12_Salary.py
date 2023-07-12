# class salary in which we are declaring a public method annual salary
# 7.1 – Create a Salary class (used by both types):

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus

