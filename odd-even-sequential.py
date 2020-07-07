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

# Groups of size 'S' with a limit of attempts to consider for this stat
largest_chunk = 400
diff = len(new) - largest_chunk
new = new[-1*largest_chunk:]

step = 25
arrs = []
for i in np.arange(0, largest_chunk, step):
	arr = new[i:i+step]
	arrs.append((arr,i,i+step))

print("Odd / Even\n")
ratios = []
for thing in arrs:
	arr = thing[0]
	odd, even = odd_even(arr)
	ratio = round(odd/even, 2)
	ratios.append(ratio)
	print("[{}]".format(",".join([str(x) for x in arr])),
		"{}/{}".format(odd,even),
		"(ratio = {})".format(ratio),
		"({} to {})".format(thing[1]+diff, thing[2]+diff))
		
plt.plot([x[2] for x in arrs] ,ratios, linestyle='--', marker='o')
plt.axhline(y=1, color='r', linestyle='-')
plt.ylabel("Ratio odd/even")
plt.xlabel("Chunks of size {}".format(step))
plt.xticks([])
plt.grid()
plt.show()