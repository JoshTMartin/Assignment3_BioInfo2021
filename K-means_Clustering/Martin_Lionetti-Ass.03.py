# Ass. 03 Martin + Lionetti
import random
import numpy as np
import pandas as pd

data = pd.read_csv("input.csv", delimiter=';', header=None)  # Importing the data from the CSV file and changing the
# delimiter from "," to ";" in order to work them. # Also, we "deleted" the header in order to work with those data
# as well.

go_topless_please = {}
name = 0
for ii in data[0][2::]:
    go_topless_please["item" + str(name)] = [float(ii.replace(",", "."))]
    name += 1

name = 0
for xx in data[1][2::]:
    go_topless_please["item" + str(name)].append(float(xx.replace(",", ".")))
    name += 1

print(go_topless_please)

centers = int(data[0][0])

print("The max and the min of coordinate x are:", max(go_topless_please[i][0] for i in go_topless_please.keys()), ",",
      min(go_topless_please[i][0] for i in go_topless_please.keys()))
print("The max and the min of coordinate y are:", max(go_topless_please[i][1] for i in go_topless_please.keys()), ",",
      min(go_topless_please[i][1] for i in go_topless_please.keys()))
# RANDOM VALUE FOR THE FIRST POSITION OF THE FIRST CLUSTER-CENTER
print("Random x coordinate (1st center)",
      (random.uniform(min(go_topless_please[i][0] for i in go_topless_please.keys()),
                      max(go_topless_please[i][0] for i in go_topless_please.keys()))))
print("Random y coordinate (1st center)",
      (random.uniform(min(go_topless_please[i][1] for i in go_topless_please.keys()),
                      max(go_topless_please[i][1] for i in go_topless_please.keys()))))

cities = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['Cities', 'Country'])

cities.to_csv("test.csv")

