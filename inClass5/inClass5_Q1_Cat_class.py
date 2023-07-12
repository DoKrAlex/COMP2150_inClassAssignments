# Question 1
class Cat:
    # A simple class
    # Attribute
    attr1 = "mammal"
    attr2 = "cat"

    # A sample method
    def fun(self):
        sound = 'meowing'  # Local variable inside fun()
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
        print("I speak by", sound)


# Driver code
# Object instantiation
lucy = Cat()
kitty = Cat()

# Accessing class attributes and method through objects
print("lucy, I am")
lucy.fun()
print("kitty, I am")
kitty.fun()

'''
Result:
lucy, I am
I'm a mammal
I'm a cat
I speak by meowing
kitty, I am
I'm a mammal
I'm a cat
I speak by meowing
'''