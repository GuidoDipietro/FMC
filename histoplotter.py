# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:04:39 2019

@author: dipie
"""

import matplotlib.pyplot as plt
import numpy as np
import sys

# Retrieving data from file into nparray

#with open("raw/rominaSingles.txt","r") as file:
with open("raw/singlesNEW.txt","r") as file:
    for line in file:
        new = line.split(", ")
        new = [int(x[0:2]) for x in new]
new = np.array(new)

# Breakpoints
breakpoints = [int(x) for x in sys.argv[1].split(',')] if len(sys.argv) > 1 else [50,100,200]

#///// Helper functions to make the code a bit less ugly

# sub mean count
def subMeanCount(lista):
	return sum(np.less(lista, lista.mean()))

# sub mean percentage
def subMeanPct(lista):
	return round((100*(subMeanCount(lista) / len(lista))),2)

# returns chunk of latest N
def chunkize(new, latest):
	return np.array(new[-1*latest:])
	
# silly string that gets printed
def subMO_N_str(latest):
	chunk = chunkize(new, latest)
	moN = round(chunk.mean() ,2)
	subMO_N_count = subMeanCount(chunk)
	subMO_N_pct = subMeanPct(chunk)
	n = latest if latest!=len(new) else "ALL"
	return f"# of sub-mo{n} ({moN}) singles last {latest}: {subMO_N_count} = {subMO_N_pct}%"

#///////////////////////////////////////////////////////

# Printing stats
for l in [len(new)] + breakpoints:
	print(subMO_N_str(l))
	
# Plotting histograms
pb = min(new)
pw = max(new)
bins = np.arange(pb,pw+2) # assures proper ticking
def hist_latest(latest):
	chunk = chunkize(new, latest)
	label = f"last {latest}" if latest!=len(new) else "lifelong"
	plt.hist(chunk, bins=bins, rwidth=0.8, label=label)

for l in [len(new)] + list(reversed(breakpoints)):
	hist_latest(l)

# Other plot details

plt.title(f"Lifelong solves + last {breakpoints}")
plt.ylabel("amount of solves")
plt.xlabel("moves")
plt.xticks([x+(1/2) for x in bins], bins, rotation=70)
plt.legend(loc='upper right')
plt.grid()
plt.show()