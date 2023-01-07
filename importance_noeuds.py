import os
import sys
import random

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
# Dans le coeur ou la périphérie
in_core = [0, 0]
in_periph = [0, 0]

# noyau principal
principal_core_nodes = nx.k_core(g).nodes
print("nbr de noeuds importants", len(node_importance))
print("max score ", max(node_importance.values()))
for node, importance in node_importance.items():
    if importance >= max(node_importance.values()) * 0.5:
        if node in principal_core_nodes:
            in_core[0] += 1
        else:
            in_periph[0] += 1
    else:
        if node in principal_core_nodes:
            in_core[1] += 1
        else:
            in_periph[1] += 1

print("score >=1/2 max(score): in_core = ", in_core[0], " in_periph = ", in_periph[0])
print("score <1/2 max(score): in_core = ", in_core[1], " in_periph = ", in_periph[1])

##################################
# Le k-coeur spécifique d'appartenance
