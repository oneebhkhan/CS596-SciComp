import matplotlib.pyplot as plt
import math
import numpy as np

processors = [1, 2, 4, 8]

strong_scaling_exec_time = [1.497344e+01, 1.354275e+01, 1.027740e+01, 1.039644e+01]
strong_scaling_efficiency = []

for index, proc in enumerate(processors):

	strong_scaling_efficiency.append( strong_scaling_exec_time[0] / (proc * strong_scaling_exec_time[index]) )


print("Strong Scaling Efficiency", strong_scaling_efficiency)

plt.plot(processors, strong_scaling_efficiency, "-og", label="Linear Fit")
plt.xlabel("Number of Threads")
plt.ylabel("Efficiency")
# plt.xticks([1,2,3,4])
plt.title("Strong Scaling Parallel Efficiency")
plt.ylim(0, 1.1)
plt.savefig("HW5_Strong_Scaling_Efficiency_Plot.png")
plt.close()

