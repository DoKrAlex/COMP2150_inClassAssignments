class Dog:
    # Class Variable
    animal = 'global animal'  # Class variable!!!

    def __init__(self, breed, color):
        # Instance variables
        self.breed = breed
        self.color = color

    def __str__(self):
        return (f' breed: {self.breed}, color: {self.color}')
    # Returns objects of Dog class

# Objects for Roger and Buzo, including breed and color
Roger = Dog("Pug", "green")
Buzo = Dog("Bulldog", "pink")

# Prints statements for Roger's and Buzo's breed + color with both objects
print('Roger details: ')
print(f'Roger is a {Roger}')

print('Buzo details: ')
print(f'Buzo is a {Buzo}')

# Class variables can be accessed using class name as well
print("\nAccessing class variable using class name")
print(f'The Dog class is: {Dog.animal}')
print("Change the class variable Dog.animal to = stuffed animal")
Dog.animal = 'stuffed animal'

print("\nNow Dog.animal is", Dog.animal, "address is ", id(Dog.animal))
print("Buzo animal is", Buzo.animal, "address is: ", id(Buzo.animal))
print("Roger animal is", Roger.animal, "address is: ", id(Roger.animal))

print("\nChange Roger to a 'Roger animal', the address before the change is ", id(Roger.animal))
Roger.animal = 'Roger animal'  # creates an instance variable for Roger
print("Roger is now a", Roger.animal, "and the address is also changed to", id(Roger.animal))

Dog.animal = "D_dog"
print(f"\nThe Dog class attribute is,{Dog.animal}, with the address {id(Dog.animal)}")
print("Buzo animal is", Buzo.animal, "with the address", id(Buzo.animal))