#Question 2
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

#2a - displaying list
print("the original list", list1)

#2b - displaying one by one
print("\neach item of list 1:")
for i in list1:
    print(i)

#2c - print list1[2]
print("\nlist1[2] is ", list1[2])

#2d - print list1[2][2]
print("\nlist1[2][2] is ", list1[2][2])

#2e - adding 7000 after 6000
print("\n")
list1[2][2].append(7000)
print(list1)

#2f - flat list
def flat(list1):
    flatList = []
    # Iterate with outer list
    for element in list1:
        if type(element) is list:
            # Check if type is list than iterate through the sublist
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)
    return flatList

print('Flat List', flat(list1))