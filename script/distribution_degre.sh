if [ "$1" == "" ]; then
    echo "ERREUR: Il faut fournir un argument (le nom du fichier)"
else
  if [ ! -f "$1" ]; then # file not found
    echo "ERREUR: Impossible de trouver le fichier passer en paramètre. Vérifiez le chemin"
  else # file found
    inputFile="$1"
    echo "Filename : $inputFile"

    # Get node with max degree
    cat $inputFile | awk '{if (NF==2) {print $1; print $2}}' | sort | uniq -c > tmp85472axy.txt

    cat tmp85472axy.txt
  fi
fi