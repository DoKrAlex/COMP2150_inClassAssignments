# Ex1: Create a class Vehicle with three instance variables (max_speed, mileage, capacity)
class Vehicle:
    def __init__(self, max_speed, mileage, capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        pass

    def m1(self):
        print(f'i am m1() from the base Class Vehicle')

    def __str__(self):
        return f' from the Vehicle (__str__) {self.max_speed}, {self.mileage}, {self.capacity}'


# Ex2: Create a child (derived) class Car-derived from the Vehicle class
class Car(Vehicle):
    def m1(self):  # m1(self): display the max_speed and mileage, Capacity, car fare)
        print(f'I am a car with a max speed of {self.max_speed}, mileage of {self.mileage}, '
              f'and a capacity of {self.capacity}')
        print(f'car fare is {self.fare()}')

    def fare(self):  # computes the fare
        return self.capacity * 0.95


# Ex3: Create a child (derived) class Bus–derived from the Vehicle class
class Bus(Vehicle):
    def m1(self):  # display the max_speed and mileage, Capacity, car fare)
        print(f'I am a bus with a max speed of {self.max_speed}, mileage of {self.mileage}, '
              f'and a capacity of {self.capacity}')
        print(f'bus fare is {self.fare()}')

    def fare(self):
        return self.capacity * 0.15

    def __str__(self):
        return f' from the Bus Class {self.max_speed}, {self.capacity}'


c1 = Car(240, 20, 40)
c1.m1()
print(c1.__str__())
print(c1)  # car class inherited the vehicle. note car(...)class does not have __str__()

print('_' * 20)

b1 = Bus(35, 8, 50)
b1.m1()
print(b1)


"""
I am a car with a max speed of 240, mileage of 20, and a capacity of 40
car fare is 38.0
 from the Vehicle (__str__) 240, 20, 40
 from the Vehicle (__str__) 240, 20, 40
____________________
I am a bus with a max speed of 35, mileage of 8, and a capacity of 50
bus fare is 7.5
 from the Bus Class 35, 50
 """