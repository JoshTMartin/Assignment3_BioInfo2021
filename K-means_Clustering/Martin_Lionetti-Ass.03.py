# Ass. 03 Martin + Lionetti
import random

import numpy as np
import pandas as pd

data = pd.read_csv("input.csv", delimiter=';', header=None)  # Importing the data from the CSV file and changing the
# delimiter from "," to ";" in order to work them. # Also, we "deleted" the header in order to work with those data
# as well.

coordinates = {}
name = 0
for ii in data[0][2::]:
    coordinates["item" + str(name)] = [float(ii.replace(",", "."))]
    name += 1

name = 0
for xx in data[1][2::]:
    coordinates["item" + str(name)].append(float(xx.replace(",", ".")))
    name += 1

print(coordinates)

centers = int(data[0][0])

print("The max and the min of coordinate x are:", max(coordinates[i][0] for i in coordinates.keys()), ",",
      min(coordinates[i][0] for i in coordinates.keys()))
print("The max and the min of coordinate y are:", max(coordinates[i][1] for i in coordinates.keys()), ",",
      min(coordinates[i][1] for i in coordinates.keys()))
# RANDOM VALUE FOR THE FIRST POSITION OF THE FIRST CLUSTER-CENTER
print(random.uniform(min(coordinates[i][0] for i in coordinates.keys()),
                     max(coordinates[i][0] for i in coordinates.keys())))
print(random.uniform(min(coordinates[i][1] for i in coordinates.keys()),
                     max(coordinates[i][1] for i in coordinates.keys())))
