import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("unlabelled_data.csv")
df.columns = df.columns.str.replace("-1.885907518189583", "x_points").str.replace("-1.997407599218205", "y_points")

x_points = [-4, 4]
y_points = [-4, 4]

lis = np.array(range(x_points[0], x_points[1]))
lis1 = np.array(range(y_points[0], y_points[1]))

k_value = len(lis1)/len(lis)
m_value = y_points[0] + (-1 * x_points[0] * k_value)

df["label"] = np.where(df["y_points"] > df["x_points"] * k_value + m_value, 0, 1)

left_side = df[df["label"] == 0]
right_side = df[df["label"] == 1]

plt.scatter(left_side["x_points"], left_side["y_points"], color = "red")
plt.scatter(right_side["x_points"], right_side["y_points"], color = "orange")
plt.plot(x_points, y_points, "b")
plt.show()