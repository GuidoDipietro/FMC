# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:15:42 2019

@author: dipie
"""

import matplotlib.pyplot as plt
import numpy as np

file = open("editedP100S.txt", "r+")
outfile= open("singles.txt", "r+")
outfile.truncate(0)
session = []

for line in file:
    session.append(int(line[-4:-2]))
    
for result in session:
    outfile.write(str(result)+",\n")
    
file.close()
outfile.close()

plt.hist(session, bins=np.linspace(20.5,41.5,22), rwidth=0.8)
plt.title("FMC avg100")
plt.ylabel("amount of solves")
plt.xlabel("moves")
plt.grid()
plt.show()