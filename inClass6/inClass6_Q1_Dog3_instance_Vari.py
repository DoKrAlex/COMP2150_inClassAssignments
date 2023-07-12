# Question 1) Modify the Cat class in “inClass5” to a Dog Class and add a ‘breed’ as an argument for the __init__(
# self, breed) function.
from turtle import color


class Dog:
    def __init__(self, breed):
        self.color = color
        self.breed = breed

    def set_color(self, color):  # this creates a instance variable
        self.color = color

    # Retrieves instance variable
    def getColor(self):
        return self.color

    def __str__(self):
        return f' breed: {self.breed}, color: {self.color}\n'


# Dog objects for Roger and Sue
Roger = Dog("pug")
Sue = Dog("lab")

# Sets colors for Roger and Sue objects
Roger.set_color("green")
Sue.set_color("pink")

# Prints statements for Roger and Sue's breed + color with both objects
print(f"Roger\'s color is {Roger.getColor()}")
print(f"Sue\'s color is {Sue.getColor()}")

print(f"\nDog Roger: {Roger}")
print(f"Dog Sue: {Sue}")
