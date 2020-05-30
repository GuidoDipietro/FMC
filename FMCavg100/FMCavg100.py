# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:34:09 2019

@author: dipie
"""

file = open("100solves.txt", "r+")
outfile = open("parsed100solves.txt", "r+")
outfile.truncate(0)

filearr = []
outfilearr = []

for line in file:
    printable = False
    for char in line:
        if (("(" in line and "'" in line) or "-" in line) and "I'" not in line:
            if char.isdigit() or char == "-": printable = True
    if printable:
        filearr.append(line)
        
for i in range(len(filearr)):
    if "-----" in filearr[i]:
        outfilearr.append(filearr[i-1])
      
for line in outfilearr:
    outfile.write(line)

file.close()
outfile.close()