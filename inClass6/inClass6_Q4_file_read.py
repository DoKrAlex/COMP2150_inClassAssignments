fname = 'test1.txt'
fp = open(fname, 'r')

# using read() read
print('using .read()---------------')
line = fp.read()
print(line)

print('using .readline()---------------')
fp.seek(0)
for i in range(3):
    print(f'{fp.readline()}')

fp.seek(0)
cont_list = [x.strip() for x in fp]
print(f'comprehensive way --------------- {cont_list}')

print('using .readlines() --------------- ')

fp.seek(0)

li1 = fp.readlines()

print(li1)
fp.close()
