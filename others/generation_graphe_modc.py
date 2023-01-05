import os.path

import networkx as nx

# co-author
filename = os.path.join(os.path.dirname(__file__), "..", "data", "small", "distribution_degree.txt")

# création de tous les degrés
list_deg = []
for line in open(filename, "r"):
    degree, nbr, percent = line.split()
    for i in range(int(nbr)):
        list_deg.append(int(degree))

g_co = nx.configuration_model(list_deg)
filename = os.path.join(os.path.dirname(__file__), "..", "data", "small", "configuration_model.txt")

with open(filename, "w") as f:
    f.write("4158\n")
    for edge in g_co.edges:
        f.write("{} {}\n".format(edge[0], edge[1]))

# # nutella
filename = os.path.join(os.path.dirname(__file__), "..", "data", "big", "distribution_degree.txt")

# création de tous les degrés
list_deg = []
for line in open(filename, "r"):
    degree, nbr, percent = line.split()
    for i in range(int(nbr)):
        list_deg.append(int(degree))

g_co = nx.configuration_model(list_deg)
filename = os.path.join(os.path.dirname(__file__), "..", "data", "big", "configuration_model.txt")

with open(filename, "w") as f:
    f.write("62561\n")
    for edge in g_co.edges:
        f.write("{} {}\n".format(edge[0], edge[1]))
