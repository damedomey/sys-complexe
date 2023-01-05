import os.path

import networkx as nx

# co-author
g_co = nx.erdos_renyi_graph(4158, 0.001)
filename = os.path.join(os.path.dirname(__file__), "..", "data", "small", "erdo_renyi.txt")

with open(filename, "w") as f:
    f.write("4158\n")
    for edge in g_co.edges:
        f.write("{} {}\n".format(edge[0], edge[1]))

# nutella
g_co = nx.erdos_renyi_graph(13422, 0.0007)
filename = os.path.join(os.path.dirname(__file__), "..", "data", "big", "erdo_renyi.txt")

with open(filename, "w") as f:
    f.write("62561\n")
    for edge in g_co.edges:
        f.write("{} {}\n".format(edge[0], edge[1]))
