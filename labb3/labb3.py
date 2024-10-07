import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("unlabelled_data.csv")
df.columns = df.columns.str.replace("-1.885907518189583", "x").str.replace("-1.997407599218205", "y")

x_points = [-4, 4]
y_points = [-4, 4]

lis = [1 for i in range(x_points[0], x_points[1])]
lis1 = [1 for i in range(y_points[0], y_points[1])]

k_value = sum(lis1)/sum(lis)
m_value = y_points[0] + (-1 * x_points[0] * k_value)

def clasifier(data, k_va, m_va = 0):
    df["label"] = df["x"]

    for x, y in zip(data["x"], data["y"]):
        alue = k_va*x + m_va
        if y > alue:
            data["label"] = data["label"].replace(x, 0)
        else:
            data["label"] = data["label"].replace(x , 1)
    
    data["label"] = data["label"].astype(int)
    return data

clasified_data = clasifier(df, k_value, m_value)
print(len(clasified_data[clasified_data["label"] == 1]))
clasified_data.to_csv("labelled_data.csv", index = False)

left_side = clasified_data[clasified_data["label"] == 0]
right_side = clasified_data[clasified_data["label"] == 1]

plt.scatter(x = left_side["x"], y = left_side["y"], color = "red")
plt.scatter(x = right_side["x"], y = right_side["y"], color = "orange")
plt.plot(x_points, y_points, "b")
plt.show()