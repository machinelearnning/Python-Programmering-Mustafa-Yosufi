import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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


def clasify_point(maj, data_x , data_y,pic_pika, wid, hei):
    points_distans =[(np.sqrt(np.power(x- wid, 2) + np.power(y- hei, 2))) 
                     for x, y in zip(data_x, data_y)]
    
    if maj == 1:

        min_value = min(points_distans)
        index_value = points_distans.index(min_value)
    
        if pic_pika[index_value] != 0:
            return 1
        else:
            return 0
    
    elif maj == 10:
        sort_values = sorted(points_distans)
        ten_values = sort_values[:10]
        index_lis_values = [points_distans.index(x) for x in ten_values]
        choose_maj = sum([pic_pika[x] for x in index_lis_values])

        if choose_maj > 5:
            return 1
        else:
            return 0
        
    else:
        print("Enter 1 or 10")
        
# köra test data med df som tränings data
predicton_testData = [(clasify_point(1, df["Width_cm"], df["Height_cm"], df["Pichu-0_pikachu-1"],x, y)) 
                      for x , y in zip(test_data["Width_cm"], test_data["Height_cm"])] 

while True:
    x_input = input("Enter your first positiv numbers.")
    y_input = input("Enter your second positiv numbers.")

    width = x_input # används för att kontrolera om ett number är negativ
    height = y_input

    x_input = x_input.replace(".", "").replace("-", "") # ta bort de karäktarer för att det skulle bli läsbar
    y_input = y_input.replace(".", "").replace("-", "")

    if x_input.isdigit() == False or y_input.isdigit() == False:
        print("You have entered a character which is not a number")
        print("You need to enter a number. ex: 23 or 34.23")
    
    width = float(width)
    height = float(height)

    if height > 0 and width > 0:
        print(clasify_point(10, df["Width_cm"], df["Height_cm"], df["Pichu-0_pikachu-1"], width, height))
        break
    elif height < 0 or width < 0:
        print("You have entered a negative number")
        print("Try again")
