#Count numbers
x = -11

while  x < 10:
    x += 1
    print(x, end = " ")

# Arithmetic sum
print()
sum = 0
i = 0
while i < 100:
    i+= 1
    sum = sum + i

print(f"the sum of this loop is: {sum}")

sum1 = 0
i1 = 0
while i1 < 100:
    i1 += 2
    sum1 = sum1 + i1

print(f"the sum of this loop is: {sum1}")

# Guess number game

import numpy as np

while True:
    random_number = np.random.randint(1, 100)
    guess_number = int(input("Guess a number between 1 to 100."))
    if random_number == guess_number:
        print("It was correct number")
    else:
        print("Your input was not correct")
    
    play_again = input("Do you want to play again! enter 'Y' for yes and'N' for no")
    if play_again == "N":
        print("Congratulaion")
        break

# Multiplication game

import numpy as np

while True:
    level = int(input("level-1(1-10)\nlevel-2(10-100)\nlevel-3(100-1000)\nInsert the number of the level you want to play."))
    if level == 1:
        random_x = np.random.randint(1, 10)
        random_y = np.random.randint(1, 10)
        multiplication = random_x * random_y
        user_guess = int(input(f"What is the answer of ({random_x} x {random_y})"))
        if user_guess == multiplication:
            print("Nice work")
            play_again = input("Do you want to play again?\n'y' for yes \n'n' for no")
            if play_again == "n":
                print("Have a good day")
                break
        else: 
            print(f"The correct answer is {multiplication}")
            play_again1 = input("Do you want to play again?\n'y' for yes \n'n' for no")
            if play_again1 == "n":
                print("Have a good day")
                break
    elif level == 2:
        random_x = np.random.randint(10, 100)
        random_y = np.random.randint(10, 100)
        multiplication = random_x * random_y
        user_guess = int(input(f"What is the answer of ({random_x} x {random_y})"))
        if user_guess == multiplication:
            print("Nice work")
            play_again = input("Do you want to play again?\n'y' for yes \n'n' for no")
            if play_again == "n":
                print("Have a good day")
                break
        else: 
            print(f"The correct answer is {multiplication}")
            play_again1 = input("Do you want to play again?\n'y' for yes \n'n' for no")
            if play_again1 == "n":
                print("Have a good day")
                break
    elif level == 3:
        random_x = np.random.randint(100, 1000)
        random_y = np.random.randint(100, 1000)
        multiplication = random_x * random_y
        user_guess = int(input(f"What is the answer of ({random_x} x {random_y})"))
        if user_guess == multiplication:
            print("Nice work")
            play_again = input("Do you want to play again?\n'y' for yes \n'n' for no")
            if play_again == "n":
                print("Have a good day")
                break
        else: 
            print(f"The correct answer is {multiplication}")
            play_again1 = input("Do you want to play again?\n'y' for yes \n'n' for no")
            if play_again1 == "n":
                print("Have a good day")
                break

# Converges a)

import numpy as np
i = 0
n = 30
sums = 1
while i < n :
    i += 1
    sums = sums + 1/np.power(2, i)
    
print(sums)

# b)

import numpy as np
i = 0
n = 5
sums = 1
while i < n :
    i += 1
    sums = sums - np.power(1, i)/(2 * i + 1)
    print(sums)
