from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import pprint
import math

# File to open
filename = "singlesNEW.txt"

# Get data into array
with open(filename,"r") as file:
    for line in file:
        new = line.split(", ")
new = [float(x) for x in new]

# Only take latest X
latest = 100
new = new[-latest:]

# Generate rolling mo3s
means = []
for k, val in enumerate(new):
	if k < (len(new)-2):
		promedio = (new[k]+new[k+1]+new[k+2])/3
		means.append(round(promedio,2))

pprint.pprint(Counter(means))

pb = math.floor(min(means)) # Best of interval
pw = math.floor(max(means)) # Worst of interval
bins = [round(x,2) for x in np.linspace(pb,pw,3*(pw-pb)+1)] # To get somewhat proper ticks
plt.figure(figsize=(10,5))
plt.hist(means, bins=bins, rwidth=0.8, align='mid', color="#009910")
plt.xticks([x+(1/6) for x in bins], bins, rotation=70)
plt.title("Count of rolling mo3s (latest {})".format(latest))
plt.ylabel("# of times I got this mo3")
plt.xlabel("Mo3 value")
plt.grid()
plt.show()