from collections import Counter
import numpy as np
import pprint
import math
import sys

# File to open
filename = "../data/__FMC_num.txt"

# Mean to count occurences of
keymean = float(input("Mean to count: "))

# Get data into array
print(f"Reading from {filename}...")
with open(filename,"r") as file:
    for line in file:
        new = line.split(", ")
new = [float(x) for x in new]

# Generate rolling mo3s
means = []
for k, val in enumerate(new):
	if k < (len(new)-2):
		promedio = (new[k]+new[k+1]+new[k+2])/3
		means.append(round(promedio,2))

# Printing result
print("")
times = sum([1 for x in means if x==keymean])
beat = sum([1 for x in means if x<keymean])
print(f"You got a {keymean} mo3 a total of {times} times.")
print(f"You beat that result a total of {beat} times.")
print(f"So all in all, less than or equal: {times+beat} times.")

input()
