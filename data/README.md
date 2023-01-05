## Extraction de composante connexe
- **data.txt** : Le fichier nettoyé. Le graphe connexe
- **correspondence.txt** : La correspondance des nœuds de 0 à n-1 dans le graphe connexe
- **rename.txt** : La correspondance des noeuds de 0 à n-1 dans le graphe initial

## Distribution des degrés
- **distribution_degree.txt** : La distribution des degrés d'un réseau. Chaque ligne contient trois données séparées par des espaces.
  - 1 - Degré
  - 2 - Nombre de noeuds
  - 3 - Nombre de noeuds en pourcentage
- **log-log_degree.png** : La distribution des degrés à l'échelle log-log
- **lin-lin_degree.png** : La distribution des degrés à l'échelle lin-lin
- **reel-erdo.png** : La distribution des degrés dans le graphe réel et un modèle d'Erdos renyi avec les mêmes paramètres

## Graphe aléatoire
- **erdo_renyi.txt** : Graphe aléatoire généré à partir des paramètres du réseau réseau réel avec le modèle d'erdo

## Distance
- **distribution_distance.[png|txt]** : La distribution des distances d'un réseau. Dans le fichier text, il y a 3 données sur chaque ligne
  - 1 - La valeur de la distance entre deux sommets
  - 2 - Le nombre de sommets réalisant cette distance
  - 3 - Le nombre de sommets réalisant cette distance en pourcentage
- **distribution_excentricité.png** : La distribution de l'excentricité dans le réseau.

## Coeur / Périphérie
