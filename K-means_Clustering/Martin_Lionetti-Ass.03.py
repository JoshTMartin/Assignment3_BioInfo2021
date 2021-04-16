import pandas as pd
import random
from matplotlib import pyplot as plt


# Function for "Manhattan distancing"
def manhattan(x, kol):
    distance = abs(coordinates['item' + str(kol)][0] - x[0]) + abs(coordinates['item' + str(kol)][1] - x[1])
    return distance


# Function for assigning each item to a specific centroid (giving them also a color and adding them to the specific
# list)
def assign(x, y, z):
    for dd in range(len(coordinates)):
        i1_center = [manhattan(x, dd), k1]
        i2_center = [manhattan(y, dd), k2]
        i3_center = [manhattan(z, dd), k3]
        close = min(i1_center, i2_center, i3_center)
        for zzz in (i1_center, i2_center, i3_center):
            if close == zzz:
                plt.scatter(coordinates['item' + str(dd)][0], coordinates['item' + str(dd)][1], c=zzz[1])
                coordinates['item' + str(dd)][2] = zzz[1]

    for sss in coordinates.items():
        if sss[1][2] == 'red':
            if sss[1] in first_color:
                pass
            else:
                first_color.append(sss[1])
        elif sss[1][2] == 'green':
            if sss[1] in second_color:
                pass
            else:
                second_color.append(sss[1])
        else:
            if sss[1] in third_color:
                pass
            else:
                third_color.append(sss[1])


# Function for finding and assigning the new position to the centroids
def new_centroids(color):
    value = 0
    value2 = 0
    if len(color) == 0:
        return [0, 0]
    for mom in color:
        value += mom[0]
        value2 += mom[1]
    return [float(value / len(color)), float(value2 / len(color))]


# Extracting the data from the csv file
data = pd.read_csv("input.csv", delimiter=';', header=None)

# Creating and filling a dictionary with each item's coordinates
coordinates = {}
name = 0
for ii in data[0][2::]:
    coordinates["item" + str(name)] = [float(ii.replace(",", "."))]
    name += 1
name = 0
for xxs in data[1][2::]:
    coordinates["item" + str(name)].append(float(xxs.replace(",", ".")))
    name += 1
# Assigning to each item a default color
for qwe in range(len(coordinates)):
    coordinates['item' + str(qwe)].append("black")

# Defining 3 different colors for each cluster and 3 different lists where to store the items of each cluster
k1 = 'red'
first_color = []
k2 = 'green'
second_color = []
k3 = 'blue'
third_color = []

# Defining 6 centers: these will be the ones that we will move and use for assign the items
centroid1 = []
centroid2 = []
centroid3 = []

new1 = []
new2 = []
new3 = []

# Function for making the whole process automatic Variable needed to choose which center variable has to be used.
counter = 0


# Basically: at the beginning this variable is obviously is zero, so the initial centers (centroid1, centroid2,
# centroid3) are being positioned randomly and the items are assigned. After each run, the counter goes up by one,
# by simply detecting if the variable counter is even/odd, "automatica()" use alternatively the second set of centers
# or the first one.
# So, in short: counter=0 automatica() fills up the variables centroid1,..,centroid3; counter=1 automatica() fills
# up the variable new1,...,new3; counter=2 automatica() fills up the variables centroid1,..,centroid3 (again); and so on


def automatica():
    global centroid1, centroid2, centroid3
    global new1, new2, new3
    global counter
    print("\n")
    if counter == 0:
        centroid1 = [random.uniform(min(coordinates[i][0] for i in coordinates.keys()),
                                    max(coordinates[i][0] for i in coordinates.keys())),
                     random.uniform(min(coordinates[i][1] for i in coordinates.keys()),
                                    max(coordinates[i][1] for i in coordinates.keys()))]
        centroid2 = [random.uniform(min(coordinates[i][0] for i in coordinates.keys()),
                                    max(coordinates[i][0] for i in coordinates.keys())),
                     random.uniform(min(coordinates[i][1] for i in coordinates.keys()),
                                    max(coordinates[i][1] for i in coordinates.keys()))]
        centroid3 = [random.uniform(min(coordinates[i][0] for i in coordinates.keys()),
                                    max(coordinates[i][0] for i in coordinates.keys())),
                     random.uniform(min(coordinates[i][1] for i in coordinates.keys()),
                                    max(coordinates[i][1] for i in coordinates.keys()))]
        assign(centroid1, centroid2, centroid3)
        for xx in coordinates.items():
            print(xx[1][2], end=", ")
        print("\nStart ", centroid1, centroid2, centroid3)
        counter += 1

    elif (counter % 2) != 0:
        new1 = new_centroids(first_color)
        new2 = new_centroids(second_color)
        new3 = new_centroids(third_color)
        assign(new1, new2, new3)
        for xx in coordinates.items():
            print(xx[1][2], end=", ")
        print("\nRun" + str(counter), new1, new2, new3)
        counter += 1
    else:
        centroid1 = new_centroids(first_color)
        centroid2 = new_centroids(second_color)
        centroid3 = new_centroids(third_color)
        assign(centroid1, centroid2, centroid3)
        for xx in coordinates.items():
            print(xx[1][2], end=", ")
        print("\nRun" + str(counter), centroid1, centroid2, centroid3)
        counter += 1


##################################

# Variable for counting the iterations of the process
iteration = 0
automatica()
while True:
    if (centroid1, centroid2, centroid3) == (new1, new2, new3):
        print("\nSince iteration", iteration, "is equal to iteration", iteration - 1,"the program ended in",
              iteration - 1, "iterations")
        break
    automatica()
    iteration += 1
