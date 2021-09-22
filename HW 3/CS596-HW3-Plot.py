import matplotlib.pyplot as plt
import math
import numpy as np

processors = [1, 2, 4]
strong_scaling_exec_time = [3.741783, 1.954865, 9.875478e-01]
weak_scaling_exec_time = [3.748947, 3.830326, 3.830135]

strong_scaling_efficiency = []
weak_scaling_efficiency = []

for index, proc in enumerate(processors):

	strong_scaling_efficiency.append( strong_scaling_exec_time[0] / (proc * strong_scaling_exec_time[index]) )

	weak_scaling_efficiency.append( weak_scaling_exec_time[0] / ( weak_scaling_exec_time[index]) )


print("Strong Scaling Efficiency", strong_scaling_efficiency)
print("Weak Scaling Efficiency", weak_scaling_efficiency)

plt.plot(processors, strong_scaling_efficiency, "-og", label="Linear Fit")
plt.xlabel("Processors")
plt.ylabel("Efficiency")
plt.xticks([1,2,3,4])
plt.title("Fix Problem-Size Parallel Efficiency")
# plt.ylim(0.94, 1)
plt.savefig("HW3_Strong_Scaling_Efficiency_Plot.png")
plt.close()

plt.plot(processors, weak_scaling_efficiency, "-or")
plt.xlabel("Processors")
plt.ylabel("Efficiency")
plt.title("Isogranular Parallel Efficiency")
# plt.ylim(0.94, 1.01)
plt.xticks([1,2,3,4])
plt.savefig("HW3_Weak_Scaling_Efficiency_Plot.png")
plt.close()
