import numpy as np

# File to open
filename = "singlesNEW.txt"

# Get data into np.array
with open(filename,"r") as file:
    for line in file:
        data = line.split(", ")

# Only using latest N
latest = 400
data = data[-1*latest:]
data = np.array([float(x) for x in data])

# Chunk size
chunk = 50

a = []
for index in reversed(np.arange(len(data)-chunk,0,-1*chunk)):
	a.append(max(data[index:index+chunk]))
a = np.array(a)
print("Partition of latest {} into chunks of {}.".format(latest, chunk))
print("Worst by chunk: ", a)
print("Mean of all: {}".format(a.mean()))
print("")

b = []
for index in reversed(np.arange(len(data)-chunk,0,-1*(chunk//2))):
	b.append(max(data[index:index+chunk]))
b = np.array(b)
print("Scan of latest {} into chunks of {}, step size = {}.".format(latest, chunk, chunk//2))
print("Worst by chunk ", b)
print("Mean of all: {}".format(b.mean()))