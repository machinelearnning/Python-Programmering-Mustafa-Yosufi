# Count numbers

for i in range(-10, 11):
    print(i, end = " ")

print( )

for i in range(-10, 11, 2):
    print(i, end = " ")

print()
# Arithmetic sum
sums = 0
for i in range(1, 101):
    sums = sums + i

print(f"The sum of the 1 to 100 is: {sums}")

sums2 = 0
for i in range(1, 101, 2):
    sums2 = sums2 + i

print(f"The sum of the 1 to 100 is: {sums2}")

# Multiplication table 
print("The table of multiplication 6.")
for i in range(1, 11):
    x = i * 6
    print(f"{i} x 6 = {x}")
# b)

table = int(input("Which table do you want to have? Insert it in number"))
start = int(input("Specify the start of the table?"))
end = int(input("specify the end of the table"))

for i in range(start, end+1):
    the_table = i * table
    print(f"{i} x {table} = {the_table}")
# c)

for i in range(0, 11):
    for x in range(0, 11):
        multi = i * x
        print(multi, end = " ")
    print()

# Faculty

n_number = int(input("Enter a number for n values."))

for i in range(1,n_number+1):
    n = (i -1)* i
    print(n)

# Guess the number

import numpy as np

digits_number = np.random.randint(1000, 9999)

for i in range(1000, 9999):
    if i == digits_number:
        print(f"The guess number is: {i}")
        print(f"The comuter numper is: {digits_number}")

# Rice on chessboard

grains_num = 1

for i in range(1, 65):
    grains_num = grains_num * 2
    print(f" The total number of grains is: {grains_num}")

