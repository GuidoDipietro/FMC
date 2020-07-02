import matplotlib.pyplot as plt
import numpy as np
import math

#with open("raw/rominaSingles.txt","r") as file:
with open("raw/singlesNEW.txt","r") as file:
    for line in file:
        new = line.split(", ")
        new = [int(x[0:2]) for x in new]
		
all = np.array(new)

# Returns odd, even
def odd_even(arr):
	odd = sum([1 for x in arr if x%2==1])
	return odd, len(arr)-odd

# Latest X from 250 to 50 skipping 50 at a time
def latest_N(n, arr):
	return np.array(arr[-1*n:])
arrs = []
for num in np.arange(250,0,-50):
	arrs.append(latest_N(num, new))

print("Odd / Even\n")
for arr in arrs:
	odd, even = odd_even(arr)
	print("{}/{}".format(odd,even),
		"(ratio = {})".format(round(odd/even, 2)),
		"(latest {})".format(len(arr)))

input()