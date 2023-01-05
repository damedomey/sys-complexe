import sys
import os

import matplotlib.pyplot as plt

from utilities import *


filename = os.path.join(os.path.dirname(__file__), sys.argv[1])
g = load_graph(filename)

n, m = g.number_of_nodes(), g.number_of_edges()
print("n = {}; m = {}".format(n, m))
print("densité = {}".format(nx.density(g)))
print("degre_moyen = {}".format(degre_moyen(g)))
print("diametre = {}".format(nx.diameter(g)))
print("distance moyenne = {}".format(nx.average_shortest_path_length(g)))

# 3 - Distribution des degrés
distribution_degree(g)

# 4 - Densité locale
print("Nombre de triangle dans le graphe")
print(get_nbr_triangles(g))
print("Coefficient de clustering local : {}".format(nx.average_clustering(g)))
print("Coefficient de clustering de chaque noeud : ")
print(nx.clustering(g))

#############################
# # Distance
# ###########################
# # Distribution des distance
# todo: calculer la distribution des distances
c_d = Counter()
distances = dict(nx.shortest_path_length(g))  # impossible de le faire sur un grand réseau, un code a donc été écrit en c pour le faire
p = 0
for source in range(n):
    for target in range(n):
        if source < target:
            c_d[distances[source][target]] += 1
            p += 1
fig, axx = plt.subplots()
fig.set_tight_layout(True)
axx.bar(c_d.keys(), [x/p for x in c_d.values()])
axx.set_title('Distribution des distances')
axx.set_xlabel("distance")
axx.set_xticks(range(max(c_d.keys())+1))
axx.set_ylabel("nb de couple (en %)")
plt.savefig(os.path.join(os.path.dirname(__file__), 'data', 'distribution_distances.png'))

# Excentricite d'un sommet
exc = nx.eccentricity(g)
c = Counter()
for i in exc.values():
    c[i] += 1

fig, (ax0, ax1) = plt.subplots(1, 2, width_ratios=[0.7, 0.3])
fig.set_tight_layout(True)
ax0.bar(c.keys(), c.values())
ax0.set_xlabel("excentricite")
ax0.set_ylabel("nb de sommets")
ax0.set_title('Distribution de l’excentricite d’un sommet')
ax1.axis('off')
for idx, value in enumerate(list(c.values())):
    ax1.text(0, idx / len(c.keys()), "{} noeuds ({}%) d'excentricité {}".format(value, round((value/n)*100, 2), list(c.keys())[idx]))

plt.savefig(os.path.join(os.path.dirname(__file__), 'data', 'distribution_excentricité.png'))

####################################
# coeur/periphérie
####################################
# evolution dans les k-coeurs
k_values = sorted(set(list(nx.core_number(g).values())))
k_nodes = []
k_wedge = []
for k in k_values:
    k_g = nx.k_core(g, k)
    k_nodes.append(k_g.number_of_nodes())
    k_wedge.append(k_g.number_of_edges())

with open(os.path.join(os.path.dirname(__file__), 'data', 'evolution_noeud_k_core'), "w") as f:
    for idx, k in enumerate(k_values):
        f.write("{} {}\n".format(k, k_nodes[idx]))

with open(os.path.join(os.path.dirname(__file__), 'data', 'evolution_arete_k_core'), "w") as f:
    for idx, k in enumerate(k_values):
        f.write("{} {}\n".format(k, k_wedge[idx]))

fig, ax = plt.subplots()
fig.set_tight_layout(True)
ax.plot(k_values, k_nodes, color='green', label='Noeuds')
ax.plot(k_values, k_wedge, color='red', label='Aretes')
ax.set_title('Evolution de n et m dans le k-coeur')
ax.set_xlabel("k")
plt.legend(loc='best')
plt.savefig(os.path.join(os.path.dirname(__file__), 'data', 'evolution_k_core.png'))

# evolution du rich club
R = g.copy()
E = R.number_of_edges()

nx.double_edge_swap(R, 100 * E, max_tries=100 * E * 10)

rcran = nx.rich_club_coefficient(R, normalized=False)
rc = nx.rich_club_coefficient(g, normalized=False)

for k, v in rc.items(): #normalisation
    if rcran[k] != 0:
        rc[k] = v/rcran[k]
    else:
        rc[k] = 0

fig2, ax3 = plt.subplots()
fig2.set_tight_layout(True)
ax3.plot(rc.keys(), rc.values())
ax3.set_title('Evolution du coefficient de rich club en fonction des degrés')
ax3.set_xlabel("degrés")
ax3.set_ylabel("rich club")
plt.savefig(os.path.join(os.path.dirname(__file__), 'data', 'evolution_rich_club.png'))
