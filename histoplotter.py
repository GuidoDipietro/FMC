# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:04:39 2019

@author: dipie
"""

import matplotlib.pyplot as plt
import numpy as np
import math

#with open("raw/rominaSingles.txt","r") as file:
with open("raw/singlesNEW.txt","r") as file:
    for line in file:
        new = line.split(", ")
        new = [int(x[0:2]) for x in new]
		
latest = 100
latest_2 = 50

new = np.array(new)
newhalf = np.array(new[-1*latest:])
#oldhalf = new[0:-1*latest]
newhalf_2 = np.array(new[-1*latest_2:])

def subMeanCount(lista):
	return sum(np.less(lista, lista.mean()))

def subMeanPct(lista):
	return round((100*(subMeanCount(lista) / len(lista))),2)

print("# of sub-moALL ({}) singles total: {} = {}%".format(round(new.mean(),2), subMeanCount(new), subMeanPct(new)))
print("# of sub-mo{} ({}) singles latest {}: {} = {}%".format(latest, round(newhalf.mean(),2),latest, subMeanCount(newhalf), subMeanPct(newhalf)))
print("# of sub-mo{} ({}) singles latest {}: {} = {}%".format(latest_2, round(newhalf_2.mean(),2),latest_2, subMeanCount(newhalf_2), subMeanPct(newhalf_2)))

pb = min(new)
pw = max(new)
bins = np.arange(pb,pw+2)

plt.hist(new, bins=bins, rwidth=0.8, label="lifelong")
plt.hist(newhalf, bins=bins, rwidth=0.8, label="latest {}".format(latest))
plt.hist(newhalf_2, bins=bins, rwidth=0.8, label="latest {}".format(latest_2))

plt.title("Lifelong solves, latest {} and latest {} solves".format(latest, latest_2))
plt.ylabel("amount of solves")
plt.xlabel("moves")
plt.xticks([x+(1/2) for x in bins], bins, rotation=70)
plt.legend(loc='upper right')
plt.grid()
plt.show()