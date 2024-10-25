import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("unlabelled_data.csv", names = ["x", "y"])

x_points = [-4, 4] 
y_points = [4, -4]

lis = np.array(range(x_points[0], x_points[-1]))
lis1 = np.array(range(y_points[-1], y_points[0]))

k_value = -len(lis1)/len(lis)
m_value = y_points[0] + ( x_points[-1] * k_value)
print(m_value, k_value)

df.to_csv("labelled_data.csv", index = False) 

# skapa en kolumn som ska innehålla om en rada klassificeras som noll eller ett.
df["label"] = np.where(df["y"] > df["x"] * k_value + m_value, 0, 1)

left_side = df[df["label"] == 0]
right_side = df[df["label"] == 1]

plt.scatter(left_side["x"], left_side["y"], color = "red")
plt.scatter(right_side["x"], right_side["y"], color = "orange")
plt.plot(x_points, y_points, "b")
plt.show()