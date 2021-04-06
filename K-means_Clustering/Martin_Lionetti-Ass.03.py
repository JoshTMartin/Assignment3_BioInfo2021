# Ass. 03 Martin + Lionetti

import numpy as np
import pandas as pd

data = pd.read_csv("input.csv", delimiter=';', header=None)  # Importing the data from the CSV file and changing the
                                                             # delimiter from "," to ";" in order to work them.
                                                             # Also, we "deleted" the header in order to work with those
                                                             # data as well.

print(data)

number = (data[0][2].replace(",", ".")) # Example on how to import  a single number for the position of the items
                                        # in the clusters

print('\n', float(number))
