# Question 3 - We use the Slice operation to print a specific range of elements from the array.
# Python program to demonstrate slicing of element in an array

# importing nlist module

import array as arr
from prt_Arr import prt

# creating a list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l)

print("Initial Array: ")
prt(a)
# print elements of a range using slice operation

Sliced_array = a[3:8]
print("\nSlicing element in a range 3-8: ")
print(Sliced_array)

# Print elements from pre-defined point to end

Sliced_array = a[5:]
print("\nElements sliced from 5th element till the end")
print(Sliced_array)

# Printing elements from beginning till end
Sliced_array = a[:]

print(f'Print element backward using slice operation:\n', Sliced_array)
back_array = a[::-1]
print("backward array", back_array)
