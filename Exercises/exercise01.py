
# Check sign

num = input("Enter a number, it can also be a negative number.")
if num  > 0:
    print("the number is positive")
elif num < 0:
    print("the number is negative")
else:
    print("the number is zero")

# Smalest

number = input("Please insert your first number.")
number1 = input("Insert your seconde number.")
samlest_number = min(number, number1)
print(f"the smalest number is: {samlest_number}")

#  Right angle

angel_1 = input("Please insert your first angel i type of number of a triangle")
angel_2 = input("Please input your second angel of a triangle")
angel_3 = input("Please input your third angel of a triangle")
sum_angels = angel_1+ angel_2 + angel_3
if sum_angels > 180 or sum_angels < 180:
    print("The sum of angels is not 180 angel")

import turtle

t = turtle.Turtle()
t.forward(100)
t.left(120)
t.forward(100)
t.left(145)
t.forward(145)

# Medicine

age = int(input("Please insert your age."))
weight = int(input("Please insert your weight just in number"))

if age > 11 and weight > 39:
    print("Ther person needs 1 or 2 pills")
elif age > 6 and age < 13 and weight > 25 and weight < 41:
    print("Ther person needs 0.5 or 1 pill")
elif age > 2 and age < 8 and weight > 14 and weight < 26:
    print("Ther person needs 0.5 pill")

# Divisible
numb = int(input("Please insert your a number without dicimal."))
divisible = numb/5 - int(numb/5)

if numb %2 == 0:
    print("The number is even")
elif numb %2 == 1:
    print("The number is odd")


if divisible == 0.0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")

if divisible == 0.0 and numb %2 == 1:
    print("The number is odd and divisible by 5")

# Luggage size

luggage = ["length", "width", "height"]
lug = []
for x in range(3):
    lug.append( int(input(f"Please insert size of {luggage[x]} in cm")))

weight = int(input("Please insert the weight of your luggaeg in kg but just number."))
if lug[0] > 55 or lug[1] > 40 or lug[2] > 23 :
    print("The size of your luggage is not the standard (50x40x23)")
if weight > 8:
    print("The weight of your luggage is not allowd")