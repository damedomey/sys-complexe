# Ce script sert juste à renomer les noeuds de 0 à n-1 dans le graphe initial J'ai dû procéder ainsi après avoir
# remarqué que les données de General Relativity ne suivent pas un ordre précis. La décrémentation classique ne marche
# donc pas.
# input: le chemin vers le fichier à traiter contenant uniquement les arrêtes
# post traitement: fichier modifier, et un fichier rename.txt contenant les correspondances
# tooltip: mon programme ne check pas les erreurs, donc en tenir compte si vous voulez l'appeler
# independament du script bash. Le script bash se charge de l'appeler avec les bonnes données.

import sys
import os

filename = os.path.join(os.path.dirname(__file__), sys.argv[1])

initial_node = []
wedge = []

for line in open(filename, "r"):
    line = line.rstrip()
    a, b = [int(x) for x in line.split(" ")]
    initial_node.append(a)
    initial_node.append(b)
    wedge.append([a, b])

# bestNode = max(initial_node, key=initial_node.count)

initial_node.sort()
s = sorted(set(initial_node))

s.sort()
new_names = [-1 for i in range(max(s)+1)]

with open("data/rename.txt", "w") as f:
    f.writelines("newname lastname\n")
    k = 0
    for i in s:
        new_names[i] = k
        f.writelines("{} {}\n".format(k, i))
        k += 1

with open(filename, "w") as f:
    for [a, b] in wedge:
        f.writelines("{} {}\n".format(new_names[a], new_names[b]))

# print(new_names[bestNode])
