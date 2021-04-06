# Ass. 03 Martin + Lionetti

import numpy as np
import pandas as pd

data = pd.read_csv("input.csv",header=None)

print(data)
n_pivot = round(data[0][0])
n_samples = round(data[0][1])
n_groups = round(data[1][1])


