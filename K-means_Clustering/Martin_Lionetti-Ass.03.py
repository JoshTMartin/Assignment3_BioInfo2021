# Ass. 03 Martin + Lionetti
import random

import numpy as np
import pandas as pd

data = pd.read_csv("input.csv", delimiter=';', header=None)  # Importing the data from the CSV file and changing the
# delimiter from "," to ";" in order to work them. # Also, we "deleted" the header in order to work with those data
# as well.

print(data)

coordinates = {}
name = 0
for ii in data[0][2::]:
    coordinates["item" + str(name)] = [ii]
    name += 1
name = 0
for xx in data[1][2::]:
    coordinates["item" + str(name)].append(xx)
    name += 1

print(coordinates)

n_cluster = int(data[0][0])

