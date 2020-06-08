# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:48:18 2020

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
        
newhalf = np.array(new[-1*latest:])
newhalf_2 = np.array(new[-1*latest_2:])

mo100 = round(newhalf.mean(),2)
mo50 = round(newhalf_2.mean(),2)
print("mo100: {}, mo50: {}".format(mo100,mo50))
print("mo100-mo50 = {}".format(round((mo100-mo50),2)))
print("mo50/mo100 = {}".format(round((mo50/mo100),2)))

pb = min(newhalf)
pw = max(newhalf)
bins = np.arange(pb,pw+2)

plt.hist(newhalf, bins=bins, rwidth=0.8, label="latest {}".format(latest))
plt.hist(newhalf_2, bins=bins, rwidth=0.8, label="latest {}".format(latest_2))

plt.title("Latest {} and latest {} solves".format(latest, latest_2))
plt.ylabel("amount of solves")
plt.xlabel("moves")
plt.xticks([x+(1/2) for x in bins], bins, rotation=70)
plt.legend(loc='upper right')
plt.grid()
plt.show()