#  EX4.1: Create three classes (Rectangle, Square, Cube) per the following UML diagram: use the same
#  rectangle class as EX4

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def __str__(self):
        return f'length: {self.length}, area: {self.area()}, perimeter: {self.perimeter()}'


# the square class inherits from the rectangle class
# square class has NO __str__()


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


class Cube(Square):
    def __init__(self, length):
        super().__init__(length)

    def surface_area(self):
        face_area = super().area()
        return face_area * self.length

    def volume(self):
        face_area = super().area()
        return face_area * self.length

    def __str__(self):
        return f'length is {self.length}, surface_area is {self.surface_area()}, volume = {self.volume}'


# Note in the Cube(b1) you have to provide an argument b1 for the square
cub1 = Cube(3)
sq1 = Square(3)

cub_area = cub1.surface_area()
cub_vol = cub1.volume()
print(f'cub(3) area = {cub_area}, volume = {cub_vol}')

print(f'The cube results: {cub1}')
print(f'The square results: {sq1}')


"""
Results:
cub(3) area = 27, volume = 27
The cube results: length is 3, surface_area is 27, volume = <bound method Cube.volume of <__main__.Cube object at 0x0000027AF2B15A90>>
The square results: length: 3, area: 9, perimeter: 12
"""