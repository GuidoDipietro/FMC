import matplotlib.pyplot as plt
import numpy as np
import math

with open("../data/__FMC_num.txt","r") as file:
    for line in file:
        new = line.split(", ")
        new = [int(x[0:2]) for x in new]
		
all = np.array(new)

# Returns odd, even
def odd_even(arr):
	odd = sum([1 for x in arr if x%2==1])
	return odd, len(arr)-odd

# Latest X from largest_chunk to 50 skipping 'step' at a time
largest_chunk = 400
step = 20
def latest_N(n, arr):
	return np.array(arr[-1*n:])
arrs = []
for num in np.arange(largest_chunk,0,-1*step):
	arrs.append(latest_N(num, new))

print("Odd / Even\n")
ratios = []
for arr in arrs:
	odd, even = odd_even(arr)
	ratio = round(odd/even, 2)
	ratios.append(ratio)
	print("{}/{}".format(odd,even),
		"(ratio = {})".format(ratio),
		"(last {})".format(len(arr)))
		
plt.plot(np.arange(-1*step,-1*largest_chunk-step,-1*step), list(reversed(ratios)))
plt.ylabel("Ratio odd/even")
plt.xlabel("Considering last -X attempts")
plt.grid()
plt.show()
