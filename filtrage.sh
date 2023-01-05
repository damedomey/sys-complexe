# Effectue le nettoyage des données
# input : le nom du fichier à nettoyer
# output : fichier nettoyer data/p2p-Gnutella31.txt

outputFile="data/data.txt"


if [ "$1" == "" ]; then
    echo "ERREUR: Il faut fournir un argument (le nom du fichier)"
else
  if [ ! -f "$1" ]; then # file not found
    echo "ERREUR: Impossible de trouver le fichier passer en paramètre. Vérifiez le chemin"
  else # file found
    inputFile="$1"
    echo "Filename : $inputFile"

    # Remove multiple space and tabulation in file
    # Sort and delete multiple wedge
    cat $inputFile |  awk -F '[ \t]+' '{
      if (NF>1 && NF<4)  {
        gsub(/[ \t]+/, "",$1);
        gsub(/[ \t]+/, "",$2);
        if ($1 == $1+0 && $2 == $2+0){
          if ($1>$2) print $2" "$1;
          else print $1" "$2;
        }
      }
     }'| sort -k1n,1 -k2n,2 | uniq >$outputFile

    # Count the nodes amount
    nbOfNode=$(cat $outputFile | awk '{print $1; print $2}' | sort -k1n,1 |uniq | wc -l)

    # Rename node from 0 to n-1 and get the best node name
    bestNode=$(python3 rename_node.py $outputFile)

    # Add number of node
    echo -e "$nbOfNode\n$(cat $outputFile)" > $outputFile

    echo "We have $nbOfNode nodes and $(($(cat $outputFile | wc -l)-1)) wedges. Perhaps not connected"

    # Get node with max degree
     bestNode=$(cat $outputFile | awk '{if (NF==2) {print $1; print $2}}' | sort | uniq -c| sort -r | head -n 1 |  awk '{print $2}')

    # Extract connected graph
    cp $outputFile tmp85472axy.txt
    make>>/dev/null;
    ./mst.out -i tmp85472axy.txt -o $outputFile -e $bestNode >>/dev/null
    rm tmp85472axy.txt

    echo "Connected graph wrote in data/data.txt and node name correspondence in data/correspondence.txt"
    echo "We have $(head $outputFile -n 1) nodes and $(($(cat $outputFile | wc -l)-1)) wedges in connected"
    echo "Done"
  fi
fi