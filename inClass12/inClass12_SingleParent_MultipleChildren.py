# Ex5: Single Parent with multiple children

"""
Program with single parent (class 1) with three children (class 4, 3, 2)
They all have a method m1().

Every child runs its own m(self) method first
"""


class Class1:
    def m(self):
        print("m() in Class1 the parent")


class Class2(Class1):
    def m(self):
        print("m() in Class2 extended from Class1")
        Class1.m(self)


class Class3(Class1):
    def m(self):
        print("m() in Class3 extended from Class1")
        Class1.m(self)
    # pass


class Class4(Class1):
    def m(self):
        print("m() in Class4 extended from Class1")
        Class1.m(self)


c4 = Class4()
c3 = Class3()
c2 = Class2()
c1 = Class1()

# create a list of class objects
# walk the list f objects Cx

ls = [c1, c2, c3, c4]
for c in ls:
    c.m()


"""
Results:
m() In Class1 the parent
m() In Class2 extended from Class1
m() In Class1 the parent
m() In Class3 extended from Class1
m() In Class1 the parent
m() In Class4 extended from Class1
m() In Class1 the parent
"""