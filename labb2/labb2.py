import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Filen är inte lämplig för direkt läsning med pandas. Med read_csv("data_points.txt", skiprows=1) hade det gått bättre
df = pd.read_csv("datapoints.txt")
df.columns = df.columns.str.replace("(", "").str.replace(")", "").str.strip().str.replace(" ", "_").str.capitalize()
df["Pichu-0_pikachu-1"] = df["Label_0-pichu"]
df = df.drop(["Label_0-pichu", "1-pikachu"], axis = 1)
# Bättre hade varit att ha korrekt data i en gemensam dataframe och filtrera efter behov
pikachu = df[df["Pichu-0_pikachu-1"] == 1] # Dela upp tränings data utifårn om det är 0 eller 1
pichu = df[df["Pichu-0_pikachu-1"] == 0]

plt.scatter(x = pichu["Width_cm"], y = pichu["Height_cm"], color = "red")
plt.scatter(x = pikachu["Width_cm"], y = pikachu["Height_cm"], color = "blue")
plt.show

# Mycket enklare hade varit att göra split(",") på raderna när du läser dem och få ut siffrorna direkt
test_list = []
with open("testpoints.txt", "r") as test_file:# spara test data rad för rad i en list
    fil = test_file.readlines()
    for line in fil:
        test_list.append(line)
# Onödigt komplicerat-- fixa datan _innan_ pandas.
test_data = pd.DataFrame(test_list, columns= ["test_d"]) # omvandla listen till en dataframe
test_data = test_data.drop(0, axis = 0)                  # göra om data till lämplig struktur
test_data["Width_cm"] = test_data["test_d"].str.split("(").str.get(1).str.split(",").str.get(0)
test_data["Height_cm"] = test_data["test_d"].str.split(")").str.get(0).str.split(",").str.get(1)
test_data = test_data.drop("test_d", axis= 1)
test_data[["Height_cm", "Width_cm"]] = test_data[["Height_cm", "Width_cm"]].astype(float)

# Denna borde ta emot en 'k' parameter istället för att hårdkoda 1 eller 10 via typ_metod
# då blir funktionen generell för alla k och behöver inte ha någon särskild hantering för fallen.
def clasify_point(typ_metod, data_x , data_y,pic_pika, wid, hei):
    points_distans =[(np.sqrt(np.power(x- wid, 2) + np.power(y- hei, 2))) 
                     for x, y in zip(data_x, data_y)]
    
    if typ_metod == 1:

        min_value = min(points_distans)
        index_value = points_distans.index(min_value)
    
        if pic_pika[index_value] != 0:
            return 1
        else:
            return 0
    
    elif typ_metod == 10:
        sort_values = sorted(points_distans)
        # detta borde var k istället för 10
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
for x , y in zip(test_data["Width_cm"], test_data["Height_cm"]):
    result = clasify_point(1, df["Width_cm"], df["Height_cm"], df["Pichu-0_pikachu-1"],x, y)
    if result == 1:
        print(f"({x},{y}): classified as Pikachu")
    else:
        print(f"({x},{y}): classified as Pichu")
 
print()
while True:
    x_input = input("Enter your first positiv numbers.")
    y_input = input("Enter your second positiv numbers.")

    width = x_input # används för att kontrolera om ett number är negativ
    height = y_input

    x_input = x_input.replace(".", "").replace("-", "") # ta bort de karäktarer för att det skulle bli läsbar
    y_input = y_input.replace(".", "").replace("-", "")

    if x_input.isdigit() == True and y_input.isdigit() == True:# koden körs när det bara är nummer.
        width = float(width)
        height = float(height)
        if height > 0 and width > 0:
            result = clasify_point(10, df["Width_cm"], df["Height_cm"], df["Pichu-0_pikachu-1"], width, height)
            if result == 1:
                print(f"({width},{height}): classified as Pikachu.")
                break
            else:
                print(f"({width},{height}): classified as Pichu.")
                break
        elif height < 0 or width < 0:
            print("You have entered a negative number")
            print("Try again")
    else:
        print("You have entered a character which is not a number")
        print("You need to enter a number. ex: 23 or 34.23")

print()
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

features = df[["Width_cm", "Height_cm"]] # features
label = df["Pichu-0_pikachu-1"] # label

# Denna uppdelning är inte balanserad, vilket krävs i uppgiften.
x_train,y_train, x_test, y_test = train_test_split(features, label, random_state = 26, test_size = 0.333)
# Dela upp  tränings data i test och tränings data.

# Nedan går att åstadkomma med reset_index()
width_training = [x for x in x_train["Width_cm"]] # ordna deras index från noll 
height_training = [x for x in x_train["Height_cm"]]
label_training= [x for x in x_test]
y_label = [x for x in y_test]

prediction10 = [(clasify_point(10, width_training, height_training, label_training, x, y)) 
                      for x, y in zip(y_train["Width_cm"], y_train["Height_cm"])]

prediction1 = [(clasify_point(1, width_training, height_training, label_training, x, y)) 
                      for x, y in zip(y_train["Width_cm"], y_train["Height_cm"])]
# Det finns mycket bättre sätt att skriva ut en confusion matrix, se ConfusionMatrixDisplay :)
con_accuraccy10 = confusion_matrix(prediction10, y_label)
con_accuraccy1 = confusion_matrix(prediction1, y_label)
print(f"performance based on majority of 10 nearest points\n", con_accuraccy10)
print(f"\nperformance based on nearest points\n", con_accuraccy1)


