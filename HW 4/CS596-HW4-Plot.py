import matplotlib.pyplot as plt
import math
import numpy as np



labels = ['Asynchronous', 'Synchronous']
async_runs = [4.786958e-01, 4.799510e-01, 4.789694e-01]
sync_runs = [5.092771e-01, 5.149350e-01, 5.079503e-01]
run_1 = [async_runs[0], sync_runs[0]]
run_2 = [async_runs[1], sync_runs[1]]
run_3 = [async_runs[2], sync_runs[2]]

x = np.arange(len(labels))  # the label locations
# print(x)
width = 0.15  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, run_1, width, label='Run 1')
rects2 = ax.bar(x, run_2, width, label='Run 2')
rects2 = ax.bar(x + width, run_3, width, label='Run 3', color='grey',)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Time (s)')
ax.set_title('Run Time Comparison of pmd_irecv.c and pmd.c')
ax.set_xticks([0,1,1.7])
ax.set_xticklabels(labels)
ax.legend()
plt.tight_layout()

plt.savefig("HW4_Part1_Time_Comparison.png")
plt.close()

datContent = [i.strip().split() for i in open("pv.dat").readlines()]
# print(datContent)

stepcount_10 = []
stepcount_20 = []
stepcount_30 = []
v10 = []
v20 = []
v30 = []
for i, element in enumerate(datContent):
	# print(element)
	if len(element) != 0:
		if i < 100:
			# print(i)
			v10.append(float(element[0]))
			stepcount_10.append(float(element[1]))
		elif i < 201:
			# print(i)
			v20.append(float(element[0]))
			stepcount_20.append(float(element[1]))
		elif i < 302:
			# print(i)
			v30.append(float(element[0]))
			stepcount_30.append(float(element[1]))

fig, ax = plt.subplots()
pdf10 = ax.plot(v10, stepcount_10, 'r', label="p(v) 10 steps")
pdf20 = ax.plot(v20, stepcount_20, 'b', label="p(v) 20 steps")
pdf30 = ax.plot(v30, stepcount_30, 'g', label="p(v) 30 steps")
# ax.set_yticks(np.arange(0,10,1))
# ax.set_xticks(np.arange(0,5,1))
ax.set_title("PDF of Velocity")
ax.set_xlabel("V")
ax.set_ylabel("P(V)")
plt.tight_layout()
ax.legend()

plt.savefig("HW4_Part2_PDF.png")
plt.close()


