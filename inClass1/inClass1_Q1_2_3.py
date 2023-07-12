#Question 1 - create empty data sets and print them out with their types
St1 = ''
ls = [ ]
d1 = { }
t1 = ( )
x = 0
y = 0,0
s = ''
b = False
st = set()
c = complex()

print('trcyvb')
print(type(ls))
print(type(d1))
print(type(t1))
print(type(x))
print(type(y))
print(type(s))
print(type(b))
print(type(st))
print(type(c))

#Question 2 - write a for loop to print names

namelist = ['Joe', 'Tom', 'Dick', 'Harry', 'Mary', 'Here', 'There', 'Everywhere']
for item in namelist:
     print(item, ',')

#Question 3 - add "What's up" to the prints
namelist = ['Joe', 'Tom', 'Dick', 'Harry', 'Mary', 'Here', 'There', 'Everywhere']
for item in namelist:
     print("What up, ", item, "?", sep="")