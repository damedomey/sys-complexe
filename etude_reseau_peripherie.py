import sys
import os
from utilities import *

filename = os.path.join(os.path.dirname(__file__), sys.argv[1])
g = load_graph(filename)

g2 = g.copy()
g2.remove_nodes_from(nx.k_core(g2).nodes)
print("base", g)
print("initial", g2) # maybe not connected
g2 = nx.subgraph(g2, max(nx.connected_components(g2), key=len))
print("connected", g2)
print("densité = {}".format(nx.density(g2)))
print("degre_moyen = {}".format(degre_moyen(g2)))
# print("diametre = {}".format(nx.diameter(g2)))
# print("distance moyenne = {}".format(nx.average_shortest_path_length(g2)))
print("Nombre de triangle dans le graphe")
print(get_nbr_triangles(g2))
print("Coefficient de clustering local : {}".format(nx.average_clustering(g2)))
# print("Coefficient de clustering de chaque noeud : ")
# print(nx.clustering(g))