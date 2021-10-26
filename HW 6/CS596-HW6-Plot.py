import matplotlib.pyplot as plt
import math

x_axis = []
y_axis = []

with open('pdf.d') as part1_output:
	lines = part1_output.readlines()
	print(lines)
	for line in lines:
		trimmed_line = line.strip('\n').split()
		
		x_axis.append(float(trimmed_line[0]))
		y_axis.append(float(trimmed_line[1]))

plt.figure(dpi=200)
plt.plot(x_axis, y_axis, "-og", label="Linear Fit", markersize=1)
plt.xlabel("r", fontsize=14)
plt.ylabel("g(r)", fontsize=14)
# plt.xticks([1,2,3,4])
plt.title("Pair Distribution Function", fontsize=18)
plt.ylim(0, 3.25)
plt.xlim(0, 25)
plt.minorticks_on()
plt.tight_layout()
plt.savefig("HW6_PDF_Plot.png")
plt.close()

