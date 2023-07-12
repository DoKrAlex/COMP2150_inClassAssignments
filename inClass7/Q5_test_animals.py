import Q5_animals as a1
c1 = a1.Cat()
print(f' what is c1 module?   {c1.__module__}')  # Q5_animals
c1.speak()
print(f"c1 is a {type(c1)} ")   # animals.Cat  (Cat is a class name)
print(f' what is c1 ? {c1}') # show just the cat object without the module name
d1 = a1.Dog()
print(f' what is d1 module?   {d1.__module__}')
d1.speak()
print(f' what is d1 ?   {d1}')

"""
Result:
what is c module?   Q5_animals
meow....
c1 is a <class 'Q5_animals.Cat'> 
 what is c1 ?   Cat....
 what is d1 module?   Q5_animals
woof *** 
 what is d1 ?   Dog****
"""