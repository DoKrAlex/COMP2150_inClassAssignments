# Ex 4: With single parent, use super( ) in the child class to initialize the attribute(s)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)  # get access to the parent.__init__


sq = Square(6)
S_area = sq.area()
print(f'sqr area is {S_area}')

rct = Rectangle(4, 5)
r_area = rct.area()
print(f'rct area is {r_area}')


"""
Results:
sqr area is 36
rct area is 20
"""