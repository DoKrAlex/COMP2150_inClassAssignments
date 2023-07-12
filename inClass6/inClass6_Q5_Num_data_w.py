#  Open a file for writing.
fn = "numbers.txt"
file = open(fn, 'w')

#  Get three numbers from user input
num1 = int(input('Enter a number: '))
num2 = int(input('Enter a second number: '))
num3 = int(input('Enter a third number: '))
print(f'You entered {num1}, {num2}, {num3}')

num1 = num2 + num3
num2 = num1 + num3
num3 = num1 + num2

print(f'New numbers are {num1}, {num2}, {num3}')

#  Write the numbers to the file.
file.write(str(num1) + '\n')
file.write(str(num2) + '\n')
file.write(str(num3) + '\n')

#  Closes outfile and prints statement that confirms that numbers have been written to it
file.close()
print(f'Data written to file {fn}, please open the file and confirm')