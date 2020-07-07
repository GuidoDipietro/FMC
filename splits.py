import numpy as np
import re
import matplotlib.pyplot as plt

#filename = "raw/clean_for_splits.txt"
filename = "raw/_FMC.txt"

dr = []
htr = []
final = []
with open(filename, "r") as file:
	for line in file:
		# Match DR
		if re.search("DR.*\(\d+\)", line): # RegEx for "...DR (num)..."
			s = re.search("\(\d+\)", line) # RegEx to return "(num)"
			dr.append(int(s.group()[1:-1])) # Just keep the number
		# Match HTR
		elif re.search("HTR.*\(\d+\)", line): # RegEx for "...DR (num)..."
			s = re.search("\(\d+\)", line) # RegEx to return "(num)"
			htr.append(int(s.group()[1:-1])) # Just keep the number
		# Match final
		elif re.search("(\d{2},\d{2},\d{2})",line):
			s = re.search("(\d{2},\d{2},\d{2})",line)
			final.append(int(s.group()[-2:]))
dr = np.array(dr)
htr = np.array(htr)
final = np.array(final)

print("DRs: ({})\n".format(len(dr)), dr)
print("Mean of all: {}\n".format(round(dr.mean(), 3)))
print("HTRs ({}):\n ".format(len(htr)), htr)
print("Mean of all: {}\n".format(round(htr.mean(), 3)))
print("All results ({}):\n".format(len(final)), final)
print("Mean of all: {}\n".format(round(final.mean(), 2)))
print("Estimated mean of finishes: {}".format(round(final.mean()-dr.mean(),2)))

def plot(graf, nparr,lab, color):
	bins = np.arange(min(nparr)-1,max(nparr)+1)
	graf.hist(nparr, bins=bins, rwidth=0.8, color=color)
	plt.xticks([x+(1/2) for x in bins], bins)
	graf.title(lab)

plt.figure()

plt.subplot(3,1,1)
plot(plt,dr,"DRs","#ff6600")

plt.subplot(3,1,2)
plot(plt,htr,"HTRs","#6666ff")

plt.subplot(3,1,3)
plot(plt,final,"Final","#595959")

# plt.subplot(2,2,4)
#plt.subplot(plt,final-dr,"Finishes (estimated)")
#To fix

plt.tight_layout(pad=1.0)

plt.show()