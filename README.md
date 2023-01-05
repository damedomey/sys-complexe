# sys-complexe

## Prise en main et filtrage des donnees
Le script **filtrage.sh** sert à faire le nettoyage des données. Il reçoit le fichier à nettoyer en
paramètre.
Le fichier nettoyer est toujours écrit dans **data/data.txt** et le fichier de correspondance de
noms de noeuds avec l'ancien nom dans **data/correspondence.txt**. Veuiller à les déplacer avant de reexécuter
le script pour éviter toute perte de données. Aussi, un fichier **rename.txt** est créé dans lequel se trouve la
correspondance des noms de noeuds avec ceux présent dans le graphe initial (de 0 à n-1, incluant tous les
sommets du graphe non connexe(peut être))
- **data/data.txt** => graphe connexe dans le bon format
- **data/correspondence.txt** => correspondance noeuds graphe non connexe et connexe
- **data/rename.txt** => correspondance noeuds de 0 à n-1 graphe non connexe et graphe initial(fichier téléchargé)


Dans le dossier **data/** se trouve toutes les données. Chaque sous dossier contient un fichier README.md qui donne
des informations concernant le nombre de noeud et d'arrêts avant et après le nettoyage.
Dans chacun des dossiers **data/*/** se trouvent tous les résultats d'analyse relative à chaque réseau.
Un fichier README.md présent dans le dossier data décrit le contenu des fichiers de chaque sous dossier.
Il faut noter que leur contenu est identique et que le dossier de sortie par défaut de tous les scripts est le 
dossier **data**
