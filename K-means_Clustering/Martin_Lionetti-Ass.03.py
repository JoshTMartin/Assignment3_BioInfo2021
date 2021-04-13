import pandas as pd
import numpy as np
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
for xx in data[1][2::]:
    coordinates["item" + str(name)].append(float(xx.replace(",", ".")))
    name += 1
# Assigning to each item a default color
for qwe in range(len(coordinates)):
    coordinates['item' + str(qwe)].append("black")

# Creating the different plots
# FIRST PLOT IS JUST THE RAW DATA

plt.subplot(2, 3, 1)

for cc in range(len(coordinates)):
    plt.scatter(coordinates['item' + str(cc)][0], coordinates['item' + str(cc)][1], c='black')
plt.title("Raw Data")
plt.xlim(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10)
plt.xticks(np.arange(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10, 0.10))
plt.ylim(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10)
plt.yticks(np.arange(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10, 0.10))
plt.grid()

# SECOND PLOT IS THE INITIAL STEP
plt.subplot(2, 3, 2)
for cc in range(len(coordinates)):
    plt.scatter(coordinates['item' + str(cc)][0], coordinates['item' + str(cc)][1], c='black')
plt.title("Start")
plt.xlim(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10)
plt.xticks(np.arange(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10, 0.10))
plt.ylim(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10)
plt.yticks(np.arange(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10, 0.10))
plt.grid()

# Defining 3 different colors for each cluster and 3 different lists where to store the items of each cluster
k1 = 'red'
first_color = []
k2 = 'green'
second_color = []
k3 = 'blue'
third_color = []

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

assign(centroid, centroid2, centroid3)



########################################################################################################################
# nn_centers = []
#
#
# def creating_clusters(puppa):
#     for xx in range(int(puppa)):
#         nn_centers.append([random.uniform(min(coordinates[i][0] for i in coordinates.keys()),
#                                           max(coordinates[i][0] for i in coordinates.keys())),
#                            random.uniform(min(coordinates[i][1] for i in coordinates.keys()),
#                                           max(coordinates[i][1] for i in coordinates.keys()))])
#
#
# # creating_clusters(data[0][0])
# # for cacca in nn_centers:
# #     plt.scatter(cacca[0], cacca[1], c="grey", marker='o', s=15 * 15)

########################################################################################################################
# THIRD PLOT - First Run of moving the centroids
plt.subplot(2, 3, 3)
plt.title("First Run")
plt.xlim(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10)
plt.xticks(np.arange(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10, 0.10))
plt.ylim(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10)
plt.yticks(np.arange(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10, 0.10))
plt.grid()
for cc in range(len(coordinates)):
    plt.scatter(coordinates['item' + str(cc)][0], coordinates['item' + str(cc)][1], c=coordinates['item' + str(cc)][2])

aa = new_centroids(first_color)
bb = new_centroids(second_color)
ccs = new_centroids(third_color)

plt.scatter(aa[0], aa[1], c=k1, marker='*', s=15 * 15)
plt.scatter(bb[0], bb[1], c=k2, marker='*', s=15 * 15)
plt.scatter(ccs[0], ccs[1], c=k3, marker='*', s=15 * 15)

assign(aa, bb, ccs)
if (aa, bb, ccs) == (centroid, centroid2, centroid3):
    print("Test ended First Run")
    plt.show()
    exit()

# Fourth PLOT - SECOND Run of moving the centroids
plt.subplot(2, 3, 4)
plt.title("Second Run")
plt.xlim(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10)
plt.xticks(np.arange(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10, 0.10))
plt.ylim(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10)
plt.yticks(np.arange(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10, 0.10))
plt.grid()
for cc in range(len(coordinates)):
    plt.scatter(coordinates['item' + str(cc)][0], coordinates['item' + str(cc)][1], c=coordinates['item' + str(cc)][2])

centroid = new_centroids(first_color)
centroid2 = new_centroids(second_color)
centroid3 = new_centroids(third_color)

plt.scatter(centroid[0], centroid[1], c=k1, marker='*', s=15 * 15)
plt.scatter(centroid2[0], centroid2[1], c=k2, marker='*', s=15 * 15)
plt.scatter(centroid3[0], centroid3[1], c=k3, marker='*', s=15 * 15)

assign(centroid, centroid2, centroid3)
if (centroid, centroid2, centroid3) == (aa, bb, ccs):
    print("Test ended Second Run")
    plt.show()
    exit()

# Fifth PLOT - THIRD Run of moving the centroids
plt.subplot(2, 3, 5)
plt.title("Third Run")
plt.xlim(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10)
plt.xticks(np.arange(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10, 0.10))
plt.ylim(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10)
plt.yticks(np.arange(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10, 0.10))
plt.grid()
for cc in range(len(coordinates)):
    plt.scatter(coordinates['item' + str(cc)][0], coordinates['item' + str(cc)][1], c=coordinates['item' + str(cc)][2])

aa = new_centroids(first_color)
bb = new_centroids(second_color)
ccs = new_centroids(third_color)

plt.scatter(aa[0], aa[1], c=k1, marker='*', s=15 * 15)
plt.scatter(bb[0], bb[1], c=k2, marker='*', s=15 * 15)
plt.scatter(ccs[0], ccs[1], c=k3, marker='*', s=15 * 15)

assign(aa, bb, ccs)
if (aa, bb, ccs) == (centroid, centroid2, centroid3):
    print("Test ended Third Run")
    plt.show()
    exit()

# Sixth PLOT - FOURTH Run of moving the centroids
plt.subplot(2, 3, 6)
plt.title("Fourth Run")
plt.xlim(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10)
plt.xticks(np.arange(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10, 0.10))
plt.ylim(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10)
plt.yticks(np.arange(0, max(coordinates[i][0] for i in coordinates.keys()) + 0.10, 0.10))
plt.grid()
for cc in range(len(coordinates)):
    plt.scatter(coordinates['item' + str(cc)][0], coordinates['item' + str(cc)][1], c=coordinates['item' + str(cc)][2])

centroid = new_centroids(first_color)
centroid2 = new_centroids(second_color)
centroid3 = new_centroids(third_color)

plt.scatter(centroid[0], centroid[1], c=k1, marker='*', s=15 * 15)
plt.scatter(centroid2[0], centroid2[1], c=k2, marker='*', s=15 * 15)
plt.scatter(centroid3[0], centroid3[1], c=k3, marker='*', s=15 * 15)

assign(centroid, centroid2, centroid3)
if (centroid, centroid2, centroid3) == (aa, bb, ccs):
    print("Test ended Fourth Run")
    plt.show()
    exit()
else:
    print("Test failed")
    exit()
