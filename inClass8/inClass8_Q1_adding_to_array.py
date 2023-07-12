# Question 1 - Exercise:  adding to an array (using array module)
# importing "array" for array creations
import array

# importing "prt_Arr" for prt function
from prt_Arr import prt


# function to convert list to an array list
def arrayList(arr):
    return arr.tolist()


# array with int type
ls1 = [1, 2, 3, 4, 5]
s1 = array.array('i', ls1)
s2 = array.array('i', [6, 7, 8, 9])

print(f'array s1 = {s1}')
print(f'array s2 = {s2}')

s3 = s1 + s2
print(f'\ncombine s3 = s1 + s2 = {s3}')  # combine the two arrays into one
print(f'add 14 to the end of s1 {s1.append(14)}')
print(s1)

s1.insert(0, 10)  # use the insert() method to add a number (10) to index location 0
print(f'\ninsert 10 at the beginning of the array: {s1}')

lst = [1, 2, 3, 4, 5, 6, 7]  # create a list (not an array) of integers and insert 'a' to the list, and print it
# do the same for the array .... what happen?
print(f'create a list {lst} and add "a" to index 3')
print(lst)
lst.insert(3, 'a')
print(f'{lst}, \n')

s1.insert(99, 100)
print(f'add 100 to index 99 of array s1 {s1}, \n')
# use extend to add another array to the end of our current array

s1.extend(s2)  # using extend(x); x is the array to be extended
print(s1)

print('\nusing the prt(x) method')
prt(s1)  # use the imported prt method to print it

print('\nconverting the array (s1) to list using arrayList(s1)')
ls = arrayList(s1)  # converting an array to list (need to have the method arrayList(arr)
print(ls)

'''
Results:
array s1= array('i', [1, 2, 3, 4, 5])
array s2= array('i', [6, 7, 8, 9])

combine s3 = s1 + s2: = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
add 14 to the end of s1 None
array('i', [1, 2, 3, 4, 5, 14])

insert 10 to the beginning of the array: array('i', [10, 1, 2, 3, 4, 5, 14])
create a list [1, 2, 3, 4, 5, 6, 7] and add "a" to index 3
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 'a', 4, 5, 6, 7],

add 100 to index 99 of array s1 array('i', [10, 1, 2, 3, 4, 5, 14, 100]),

array('i', [10, 1, 2, 3, 4, 5, 14, 100, 6, 7, 8, 9])

using the prt(x) method
10 1 2 3 4 5 14 100 6 7 8 9

converting the array (s1) to list using arrayList(s1)
[10, 1, 2, 3, 4, 5, 14, 100, 6, 7, 8, 9]
'''
