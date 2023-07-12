#  Q5) __module__ attribute as a class (data type), object, with __str__ to display its type.
# Create two modules (Q5_animals.py and Q5_test_animals.py)
'''
  Import this module (Q5_animals.py)  to Q5_use_animals_module_mclass.py and run it in class.
  comment out the __str__(self) and run it again...
'''
class Cat:
    att1 = "Cat...."
    def speak(self):
        print("meow....")
    def __str__(self):
        return self.att1
class Dog:
    att1 = "Dog****"
    def speak(self):
        print('woof *** ')
    def __str__(self):
        return self.att1