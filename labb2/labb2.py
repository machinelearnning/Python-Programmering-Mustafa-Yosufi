import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datapoints.txt")
df.columns = df.columns.str.replace("(", "").str.replace(")", "").str.strip().str.replace(" ", "_").str.capitalize()
df["Pichu-0_pikachu-1"] = df["Label_0-pichu"]
df = df.drop(["Label_0-pichu", "1-pikachu"], axis = 1)

pikachu = df[df["Pichu-0_pikachu-1"] == 1]
pichu = df[df["Pichu-0_pikachu-1"] == 0]

plt.scatter(x = pichu["Width_cm"], y = pichu["Height_cm"], color = "red")
plt.scatter(x = pikachu["Width_cm"], y = pikachu["Height_cm"], color = "blue")
plt.show

test_list = []
with open("testpoints.txt", "r") as test_file:
    fil = test_file.readlines()
    for line in fil:
        test_list.append(line)

test_data = pd.DataFrame(test_list, columns= ["test_d"]) # omvandla listen till en dataframe
test_data = test_data.drop(0, axis = 0)                  # göra om data till lämplig struktur
test_data["Width_cm"] = test_data["test_d"].str.split("(").str.get(1).str.split(",").str.get(0)
test_data["Height_cm"] = test_data["test_d"].str.split(")").str.get(0).str.split(",").str.get(1)
test_data = test_data.drop("test_d", axis= 1)
test_data[["Height_cm", "Width_cm"]] = test_data[["Height_cm", "Width_cm"]].astype(float)
print(test_data)



