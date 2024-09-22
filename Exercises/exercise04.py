# Dice rolls
deci10 = list((2, 3, 3, 1, 2, 5, 6, 2, 4, 6))
sort_deci = sorted(deci10)
print(sort_deci)
print(sort_deci[::-1])
print(f"Maximum {max(deci10)} \nMinimum {min(deci10)}")

# Food menu

food_menu = ["vegetarisk lasagne", "spaghetti", "fisk", "grönsakssoppa", "pannkakor"]
week_days = ["Mån", "Tis", "Ond", "Tor", "Fre"]

for i in range(5):
    print(f"{week_days[i]}: {food_menu[i]}")

# Squares
import matplotlib.pyplot as plt
import numpy as np
list = [x for x in range(-10, 11)]

plt.plot(np.power(list, 2))
plt.show()

# Chessboard

list1 = ["ABCDEFGH"]
list2 = [x for x in len(list1)]
print(list2)

# b)

name_list = "ABCDEFGH"

leer = [[f"{i}{x+1}" for i in name_list]for x in range(8)]
for x in leer:
    print(x)

# Dice rolls convergence
sums = 0
for x in range(100):
    deci_nu = np.random.randint(7)
    if deci_nu == 6:
        sums = sums + 1

print(sums)

# b)

import numpy as np
import matplotlib.pyplot as plt

asemulation = [10, 100, 1000, 10_000, 100_000, 1000_000]
lis_deci = []
sum_deci1 = 0
           
for x in range(6):
    for i in range(asemulation[x]):
        deci_multi = np.random.randint(7)
        if deci_multi == 6:
            sum_deci1 = sum_deci1 + 1

    lis_deci.append(sum_deci1)
    sum_deci1 = sum_deci1 - sum_deci1
    

probability = []

for x in range(6):
    probability.append(lis_deci[x] / asemulation[x])

np.random.seed(1)

plt.plot(probability, '-*')
plt.title("Probability of six for different number of rolls")
plt.xticks([0, 1, 2, 3, 4, 5], asemulation)
plt.xlabel("Number of dice rolls")
plt.ylabel("Probability")
plt.show()

# Monte Carlo simulation

import numpy as np
import matplotlib.pylab as plt

x = np.random.uniform(-1, 1, 5000)
y = np.random.uniform(-1, 1, 5000)

nd = np.sqrt(np.power(x, 2) + np.power(y, 2))
inside = nd <= 1
outside  =nd >= 1

plt.scatter(x[inside], y[inside], color = "red")
plt.scatter(x[outside], y[outside], color = "green")
plt.show()

# b)

num_inside = np.sum(inside)
num_outside = np.sum(outside)

# fraction = dividign. converge = get closing to number or value
fraction = num_inside/num_outside
print(fraction)

#  A cute rabbit among two ferocious snakes
# a) The obtion switch has more chanse to find the rabit becaus I have (2 of 3) instead of (1 of 3)

# B

import numpy as np
import matplotlib.pyplot as plt 

test_num = [10, 100, 1000, 10_000, 100_000, 1000_000]

option = ["Rabit", "Snackes" ]
switch = ["Stay", "Switch"]

stay_rabit = 0
switch_rabit = 0

stay_rabit_li = []
switch_rabit_li = []
    
        
for x in range(6):
    for i in range(test_num[x]):
        random_choose = np.random.randint(2)
        random_choose2 = np.random.randint(2)
        chose_dorr = option[random_choose]
        stay_switch = switch[random_choose2]

        if chose_dorr == "Rabit":
            if stay_switch == "Stay":
               stay_rabit = stay_rabit + 1

        if chose_dorr == "Rabit":
            if stay_switch == "Switch":
               switch_rabit = switch_rabit + 1

    stay_rabit_li.append(stay_rabit)
    switch_rabit_li.append(switch_rabit)
    stay_rabit = stay_rabit - stay_rabit
    switch_rabit = switch_rabit - switch_rabit
    
print(stay_rabit_li)
print(switch_rabit_li)

stay_pro = []
switch_pro = []

for i in range(6):
    stay_pro.append(stay_rabit_li[i]/test_num[i])
    switch_pro.append(switch_rabit_li[i]/test_num[i])


plt.plot(stay_pro, ":or", label = "Stay")
plt.plot(switch_pro, ":og", label = "Switch")
plt.xticks([0,1,2,3,4,5], test_num)
plt.xlabel("Number of asemulation")
plt.ylabel("Proportion wins")
plt.title("Proportion of win are 2/3 compared to 1/3 when switching")
plt.legend()
plt.show()




