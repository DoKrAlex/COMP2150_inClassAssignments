#Question 1
lst1 = [1, 3, 5, 7, 8]

#Standard for loop with the list [1, 3, 5, 7, 8]
def for_i(lst1):
    for i in lst1:
        print(i, end = ", ")

#for loop with range()
def for_range(lst1):
    for i in range(5):
        print(lst1[i], end = ", ")

#while loop
def while_i(lst1):
    i = 0
    while i < len(lst1):
        print(lst1[i], end = ", ")
        i = i + 1

#List comprehension
def list_comprehension(lst1):
    [print(x, end = ", ") for x in lst1]

print("for_i")
for_i(lst1)
print("\nfor_range")
for_range(lst1)
print("\nwhile_i")
while_i(lst1)
print("\nlist comprehension")
list_comprehension(lst1)