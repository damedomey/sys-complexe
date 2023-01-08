import os
import sys
import random

import networkx as nx
from matplotlib import pyplot as plt

from utilities import *

##################################################################
# Traitements relatifs à l'importance des noeuds dans le reseau  #
# (Etude du positionnement des noeuds les plus important)        #
##################################################################
filename = os.path.join(os.path.dirname(__file__), sys.argv[1])
g = get_graph_sample(filename, node_limit=15000)

print(g)

node_importance = get_node_importance(g)

################################
# # Dans le coeur ou la périphérie
# in_core = [0, 0]
# in_periph = [0, 0]
#
# # noyau principal
# principal_core_nodes = nx.k_core(g).nodes
# print("nbr de noeuds importants", len(node_importance))
# print("max score ", max(node_importance.values()))
# for node, importance in node_importance.items():
#     if importance >= max(node_importance.values()) * 0.5:
#         if node in principal_core_nodes:
#             in_core[0] += 1
#         else:
#             in_periph[0] += 1
#     else:
#         if node in principal_core_nodes:
#             in_core[1] += 1
#         else:
#             in_periph[1] += 1
#
# print("score >=1/2 max(score): in_core = ", in_core[0], " in_periph = ", in_periph[0])
# print("score <1/2 max(score): in_core = ", in_core[1], " in_periph = ", in_periph[1])

##################################
# Le k-coeur spécifique d'appartenance
cores = sorted(set(list(nx.core_number(g).values())))
k_nodes = []
k_core = []
for k in cores:
    k_nodes.append([x for x in nx.k_core(g, k).nodes()])
    k_core.append(k)
    # k_nodes.append(len(list(set(k_g.nodes()).intersection(node_importance.keys()))))

# redéfinition des couches pour qu'un noeuds ne soit présent dans plusieurs couches
for idx, core_nodes in enumerate(k_nodes):
    if idx < len(k_nodes)-1:
        for node in k_nodes[idx + 1]:
            k_nodes[idx].remove(node)

fig, ax = plt.subplots()
fig.set_tight_layout(True)
ax.plot(cores, [len(x) for x in k_nodes], marker='o')
ax.set_title('Evolution de noeud important dans le k-coeur')
ax.set_xlabel("k")
plt.savefig(os.path.join(os.path.dirname(__file__), 'data', 'noeud_important.png'))

