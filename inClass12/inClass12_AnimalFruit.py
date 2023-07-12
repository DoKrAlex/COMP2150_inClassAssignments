# EX 8 Polymorphism
from abc import ABC, abstractmethod


# Ex 8.1 Create two classes (Food and Animal) with ABC as their parent


class Food(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def how_to_eat(self):
        pass

    def __str__(self):
        return self.name


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    def __str__(self):
        return {self.name}


# Create four classes (Dog, Cat, Fish, Chicken)

class Cat(Animal):
    def __init__(self, age):
        super().__init__(name='cat')
        self.age = age

    def speak(self):
        print("the cat says meow")

    def __str__(self):
        return f' {self.name}, age = {self.age}, {self.speak()}'


class Dog(Animal):
    def __init__(self, age):
        super().__init__(name='dog')
        self.age = age

    def speak(self):
        print("the dog says woof")

    def __str__(self):
        return f' {self.name}, age = {self.age}, {self.speak()}'


class Chicken(Animal, Food):
    def __init__(self, age):
        super().__init__(name='chicken')
        self.age = age

    def speak(self):
        print("the chicken says gog gog gog")

    def how_to_eat(self):
        print("chicken: fried, grilled, charred, over salad")

    def __str__(self):
        return f' {self.name}, age = {self.age}'

# Create two classes (Apple, Orange)


class Apple(Food):
    def __init__(self):
        super().__init__(name='Apple')

    def how_to_eat(self):
        print("apple: bite, juice, slice, slurp")


class Orange(Food):
    def __init__(self):
        super().__init__(name='orange')

    def how_to_eat(self):
        print("orange: peel, squeeze, juice")


class Fish(Animal, Food):
    def __init__(self):
        super().__init__(name='fish')

    def speak(self):
        print("the fish says glub glub glub")

    def how_to_eat(self):
        print("fish: filet, baked, seared, fried, steamed, broiled")

# Driver codes (test codes)
# Create five objects for the above five classes


c1 = Cat(999)
d1 = Dog(50)
a1 = Apple()
o1 = Orange()
f1 = Fish()
chk = Chicken(5)

# Create a list of animal type, food type, and every type

animal_ls = [c1, d1, f1, chk]
food_ls = [o1, a1, f1, chk]
all_ls = [c1, d1, a1, o1, f1, chk]

# Use a for loop in all types to exercise the speak() and how_to_eat() method

print('Animal speech: ')
for x in animal_ls:
    x.speak()

print('\nways to eat: ')
for eat in food_ls:
    eat.how_to_eat()

print('\ncheck using ininstance(...)')
for y in all_ls:
    if isinstance(y, Animal):
        y.speak()
    elif isinstance(y, Food):
        y.how_to_eat()


"""
Results
Animal speech: 
the cat says meow
the dog says woof
the fish says glub glub glub
the chicken says gog gog gog

ways to eat: 
orange: peel, squeeze, juice
apple: bite, juice, slice, slurp
fish: filet, baked, seared, fried, steamed, broiled
chicken: fried, grilled, charred, over salad

check using ininstance(...)
the cat says meow
the dog says woof
apple: bite, juice, slice, slurp
orange: peel, squeeze, juice
the fish says glub glub glub
the chicken says gog gog gog
"""