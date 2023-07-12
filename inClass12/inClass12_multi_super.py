# Ex6: multiple levels and multiple inheritances.

"""
Class1 - "root"
Class 2, 3 extends from Class 1
"""


class Class1:
    def m(self):
        print("in Class1 the parent")


class Class2(Class1):
    def m(self):
        print("in Class2 extended from C1")
        super().m()


class Class3(Class1):
    def m(self):
        print("in Class3 extended from C1")
        super().m()


class Class4(Class3, Class2):
    def m(self):
        print("in Class4 extended from C2, C3")
        super().m()


c4 = Class4()
# note c4 chains to c2, c3 and to c1
c4.m()

"""
result:
In Class4 extended from C2, C3
In Class2 extended from C1
In Class3 extended from C1
In Class1
change to order of Class3, Class2 in Class4 and run it again
"""