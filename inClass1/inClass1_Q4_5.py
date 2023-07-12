#Question 4 - write for loop to display amount of characters in string
string = 'Heaven can wait'
count = 0
for letter in string:
    count = count + 1
print('The number of characters in the string "', string, '" is ', count, sep='')

#Question 5
#5a
list = ['Heaven can wait', '123', 'abcde']
print(list)

#5b
for item in list:
    print(item)

#5c
x = 0
for letter in list[0]:
    x += 1
    y = x
x = 0
for letter in list[1]:
    x += 1
    z = x
x = 0
for letter in list[2]:
    x += 1
    aa = x
x = 0
print('Number of characters of item[0] is', y)
print('Number of characters of item[1] is', z)
print('Number of characters of item[2] is', aa)

#5d
newlist = []
newlist.append(y)
newlist.append(z)
newlist.append(aa)
print(newlist)

#5e
print('The sum of newlist is ', sum(newlist))