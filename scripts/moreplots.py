# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:44:04 2019

@author: dipie
"""

import matplotlib.pyplot as plt
import numpy as np

with open("../data/__FMC_num.txt","r") as file:
    for line in file:
        data = list(enumerate([int(x[0:2]) for x in line.split(", ")]))
        data = np.array([(x,y) for x,y in data])
        
x = data[:,0]
y = data[:,1]

plt.plot(y, "ro")
plt.xlabel("solve number")
plt.ylabel("movecount")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
plt.show()
