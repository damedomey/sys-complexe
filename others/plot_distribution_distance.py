# plot the distribution of distance from file
import os

from matplotlib import pyplot as plt


filename = os.path.join(os.path.dirname(__file__), "..", "data", "distribution_distance.txt")
distance_list = []
percent_list = []
for line in open(filename, "r"):
    if len(line.split()) == 3:
        distance, count, percent = [float(x) for x in line.rstrip().split(" ")]
        distance_list.append(distance)
        percent_list.append(percent)

fig, ax = plt.subplots()
fig.set_tight_layout(True)
ax.bar(distance_list, percent_list)
ax.set_title('Distribution des distances')
ax.set_xlabel("distance")
ax.set_xticks(range(int(max(distance_list))+1))
ax.set_ylabel("nb de couple (en %)")
plt.savefig(os.path.join(os.path.dirname(__file__), "..", 'data', 'distribution_distance.png'))
