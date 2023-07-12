# Question 2
class Cat2:
    def __init__(self):
        self.name = ""

    # The sample method
    def say_hi(self):
        print(self.name, 'meow')

    def __str__(self):  # " function used to display the object attributes (i.e. name)
        return f'cat names is {self.name}'


# Creating two objects (p1, p2) as (Lucy, Kitty)
p1 = Cat2()
p1.name = "Lucy"
p1.say_hi()

p2 = Cat2()
p2.name = "Kitty"
p2.say_hi()

# Condition to create an object p3 and print(p3)
x = 5
if x == 5:
    p3 = Cat2()
    p3.name = "Blackie"
    print(p3)

'''
Result:
Lucy meow
Kitty meow
cat names is Blackie
'''