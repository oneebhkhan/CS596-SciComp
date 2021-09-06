import matplotlib.pyplot as plt
import math
import numpy as np

N = [4000, 13500, 32000, 62500]
T = [0.57101, 5.8720, 32.122, 121.95] 

logN = np.log10(N)
logT = np.log10(T)
NUM_ELEMENTS = 4

print("Log N", logN)
print("Log T", logT)

plt.plot(logN, logT)
plt.xlabel("log(N)")
plt.ylabel("log(T)")
plt.title("Molecular Dynamics: log(T) vs. log(N)")
plt.savefig("HW1-MDTime-Plot.png")

point1 = [logN[0], logT[0]]
point2 = [logN[3], logT[3]]

alpha = (point1[1] - point2[1]) / (point1[0] - point2[0])

beta = logT[3] - (alpha * logN[3])

print("Alpha:", alpha)
print("Beta:", beta)

print("LEAST SQUARE FIT")

a = ((4 * np.dot(logN, logT)) - (np.sum(logN) * np.sum(logT))) / \
	( np.sum(np.multiply(np.square(logN), NUM_ELEMENTS)) - np.square(np.sum(logN)) )

b = ( -1*(np.sum(logN)*np.dot(logN, logT)) + (np.sum(np.square(logN))*np.sum(logT)) ) / \
	( np.sum(np.multiply(np.square(logN), NUM_ELEMENTS)) - np.square(np.sum(logN)) )

print("a: ", a)
print("b:", b)