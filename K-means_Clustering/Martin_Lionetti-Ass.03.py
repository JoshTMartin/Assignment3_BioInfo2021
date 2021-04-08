# Ass. 03 Martin + Lionetti

import numpy as np
import pandas as pd

data = pd.read_csv("input.csv", delimiter=';', header=None)  # Importing the data from the CSV file and changing the
                                                             # delimiter from "," to ";" in order to work them.
                                                             # Also, we "deleted" the header in order to work with those
                                                             # data as well.

print(data)

A_positions = []
for ii in data[0][2::]:
    A_positions.append(float(ii.replace(",",".")))

print(A_positions)

B_position = []
for oo in data[1][2::]:
    B_position.append(float(oo.replace(",",".")))

print(B_position)
