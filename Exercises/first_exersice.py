import numpy as np

a = 3
b = 4
3
hypo = np.sqrt(np.power(a, 2) + np.power(b, 2))
print(f"The hypothenus is {hypo}")

c = 7.0
d = 5.0

cath = np.sqrt(np.power(c, 2) - np.power(d, 2))
print(f"The cathetus is {round(cath, 1)}")

# Calculate of the accurracy of the model
tp = 2
tn = 985
fp = 2
fn = 11

calcul = (tp + tn)/(tp + tn + fp + fn)
print(f"the accurracy is {calcul}")

# 
A = (4, 4)
B  =(0, 1)
x = (A[0]-B[0])
y = (A[1]-B[1])
k = y/x
m = B[1]
print(f"The equation is: y = {k}x + {m}")

# Euclidean distance
p1 = (3, 5)
p2 = (-2, 4)

distance = np.sqrt(np.power((p1[0]-p2[-2]), 2) + np.power((p1[1] - p2[1]), 2))
print(f"The distance is: {round(distance, 1)}")

# Euclidean distance in 3D 

x1 = (2, 1, 4)
x2 = (3, 1, 0)

distan = np.sqrt(np.power((x1[0] - x2[0]), 2) + np.power((x1[1] - x2[1]), 2) + np.power((x1[2] - x2[2]), 2))
print(f"The distance between p and q is: {round(distan, 2)}")