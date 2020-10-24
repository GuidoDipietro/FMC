import numpy as np

# File to open
filename = "raw/singlesNEW.txt"
#filename = "raw/rominaSingles.txt"
#filename = "raw/gustavoSingles.txt"

# Get data into np.array
with open(filename,"r") as file:
    for line in file:
        data = line.split(", ")

# Only using latest N
latest = 74
data = data[-1*latest:]
data = np.array([float(x) for x in data])

# chunk size
chunk_size = 10
step_size = 5

######## Partition approach ########

a = [[],[],[]]
for index in reversed(np.arange(len(data)-chunk_size,0,-1*chunk_size)):
	chunk = data[index:index+chunk_size]
	a[0].append(max(chunk))
	a[1].append(np.unique(chunk)[-2])
	a[2].append(np.unique(chunk)[-3])
a = np.array(a)
print("Partition of last {} into chunks of {}.".format(latest, chunk_size))
print("Worst by chunk: {}, mean = {}".format(a[0], round(a[0].mean(), 2)))
print("2nd worst by chunk: {}, mean = {}".format(a[1], round(a[1].mean(), 2)))
print("3rd worst by chunk: {}, mean = {}".format(a[2], round(a[2].mean(), 2)))
print("")

######## Scan approach ########

b = [[],[],[]]
for index in reversed(np.arange(len(data)-chunk_size,0,-1*step_size)):
	chunk = data[index:index+chunk_size]
	b[0].append(max(chunk))
	b[1].append(np.unique(chunk)[-2])
	b[2].append(np.unique(chunk)[-3])
b = np.array(b)
print("Scan of last {} into chunks of {}, step size = {}.".format(latest, chunk_size, step_size))
print("Worst by chunk: {}, mean = {}".format(b[0], round(a[0].mean(), 2)))
print("2nd worst by chunk: {}, mean = {}".format(b[1], round(a[1].mean(), 2)))
print("3rd worst by chunk: {}, mean = {}".format(b[2], round(a[2].mean(), 2)))

input()
# If executed by double-click