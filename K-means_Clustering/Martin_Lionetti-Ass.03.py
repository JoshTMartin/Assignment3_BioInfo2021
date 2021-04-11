import pandas as pd
import numpy as np
import random
from matplotlib import pyplot as plt

# Extracting the data from the csv file
data = pd.read_csv("input.csv", delimiter=';', header=None)

# Creating and filling a dictionary with each item's coordinates
coordinates = {}
name = 0
for ii in data[0][2::]:
    coordinates["item" + str(name)] = [float(ii.replace(",", "."))]
    name += 1
name = 0
for xx in data[1][2::]:
    coordinates["item" + str(name)].append(float(xx.replace(",", ".")))
    name += 1

# Creating the first plot
fig = plt.plot(figsize=(5, 5))
plt.title("First Run")
plt.xlim(0, 1)
plt.xticks(np.arange(0, 1.10, 0.10))
plt.xlabel("X-axis")
plt.ylim(0, 1)
plt.yticks(np.arange(0, 1.10, 0.10))
plt.ylabel("Y-axis")

# Plotting the different items
for cc in range(len(coordinates)):
    plt.scatter(coordinates['item' + str(cc)][0], coordinates['item' + str(cc)][1], c='black')

# Assigning to each center a specific color
k1 = 'red'
k2 = 'green'
k3 = 'blue'

# Creating 3 different random centroids using the min/max of the data
centroid = [random.uniform(min(coordinates[i][0] for i in coordinates.keys()),
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

# Adding the centroids to the plot
plt.scatter(centroid[0], centroid[1], c=k1, marker='*', s=15 * 15)
plt.scatter(centroid2[0], centroid2[1], c=k2, marker='*', s=15 * 15)
plt.scatter(centroid3[0], centroid3[1], c=k3, marker='*', s=15 * 15)


# Function for "Manhattan distancing"
def manhattan(x, j):
    distance = abs(coordinates['item' + str(j)][0] - x[0]) + abs(coordinates['item' + str(j)][1] - x[1])
    return distance


# Function for assigning each item to a specific centroid (giving them also a color)
def assign(x, y, z):
    for dd in range(len(coordinates)):
        i1_center = [manhattan(x, dd), k1]
        i2_center = [manhattan(y, dd), k2]
        i3_center = [manhattan(z, dd), k3]
        close = min(i1_center, i2_center, i3_center)
        for zzz in (i1_center, i2_center, i3_center):
            if close == zzz:
                plt.scatter(coordinates['item' + str(dd)][0], coordinates['item' + str(dd)][1], c=zzz[1])


assign(centroid, centroid2, centroid3)


# Displaying the results
plt.show()

# TODO NEW CENTROIDS (MEAN OF FOUND ITEMS) AND REALLOCATION
