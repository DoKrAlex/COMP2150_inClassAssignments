# Question 2 - exercise: ways to remove elements from an array
# using del method [i]: i is the index location
# important "nlist" for nlist operation
import array


# removing all reoccurring numbers

def rm_all(arr, r_item):
    for item in arr:
        if item == r_item:
            arr.remove(r_item)


arr = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 8])

# printing original nlist
print("The new created arr is: ", end="")

print(arr)

# using del method [1]: i is

print(f'delete element arr[1]')
del arr[1]
print(arr)

# using pop(2) to remove element at second position
print("The popped element is: ", end="")
print(arr.pop(2))

print(arr)
print(f'\npopping the last element: {arr.pop()}')

print(arr)

# using remove to remove ls
arr.remove(1)
print("\nThe arr after removing 1 is: ", end="")
print(arr)

# count the number of occurrences

rm_item = 9

print(f'\nThe occurrence of {rm_item} is {arr.count(rm_item)}')

# Remove all instances of particular instances
print("\nRemoves all occurrences of 9")
arr.remove(rm_item)
print(arr)

# Find index of particular instance
rm_item = 7
print(f'\nLocation of {rm_item} is in {arr.index(rm_item)}')




