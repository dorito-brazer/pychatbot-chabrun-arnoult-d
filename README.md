# Mathieu Chabrun Quentin Arnoult
#pychatbot-chabrun-arnoult-d

Explication des fonctions du programme : 

ligne 7 : Fonction : ( list_of_file )==> Recupere le nom des fichiers contenant les dicsours contenus dans le dossier speeches et le stocke dans la liste files_names

ligne 14 : Fonction : ( minuscules ) ==> Cette fonction renvoie une liste de listes, dans laquelle chaquz sous liste contient des mots d'une ligne d'un fichier où les caractères majuscules sont transformés en caractères minuscules et où la pnctuation est effacée. En gros elle réécris les discours en transformant tous les caractères majuscules en minuscules, enlèves les caractères spéciaux ,.;:?!- et stocke dans une liste lst1 tout le texte transformé. 

ligne 33 : Fonction : ( nom_president ) ==> En important le nom des fichiers depuis la liste files_names, il nettoie le titre du fichier en enlevant tous les caractères spéciaux ou non de façon a retourner uniquement le nom du président et le stocke dans une liste names

ligne 40 : Fonction ( fish_to_name ) ==>  Sous-fonction de nom president. Prend un fichier spécifique et renvoie le nom du président associé au fichier 

ligne 48 : Fonction : ( write ) ==> Cette fonction prend un nom de fichier, récupère sa version convertie en minuscule et écrit le contenu converti dans un nouveau fichier dans le dossier "cleaned" avec le même nom qu'il avait avant d'etre transformé

ligne 58 : Fonction : ( prenom ) ==> Cette fonction associe, dans un dictionnaire nommé prenom le prénom d'un président à son nom

ligne 67 : Fonction : ( fich_to_list ) ==> Cette fonction est presque identique à la fonction minuscule a la seule différence qu'elle remplace les ' et les - par des espaces 

ligne 84 : Fonction : ( dictionnaire ) ==> Calcule le nombre d'occurence de chaque mot d'un tableau et le stock dans un dico sous la forme mot : occurence

ligne 102 : Fonction : ( calcul_idf ) ==> Calcule, avec le nombre d'occurence de chaque mot, le log en base 10 de ce motavec la formule idf=og((nombre_total_de_fichiers / nombre_de_fichiers_contenant_le_mot) + 1, 10), arrondis à 3 chiffees après la virgule

ligne 109 : Fonction ( score_tf_idf ) ==> Cette fonction utilise le score tf et le score idf. Elle calcule d'abord le score tf dans la matrcie dico_tf. Enfin, elle multiplie le score tf et le score idf pour avoir le score_tf_idf qui représente l'importance de chaque mot dans tous les fichiers  

ligne 117 : Fonction ( matrice ) ==> Créer une matrcie et ffiche, comme nombre de lignes le nombre de mots uniques dans tous les fichiers et le nombre de colonnes est égal au nombre de fichiers dans le répertoire

ligne 129 : Fonction ( mots_pas_imp ) ==> Cette fonction parcours les éléments de la matrice et a pour but de trouver les mots les - importants, c'est à dire que son score tf_idf=0. Elle renvoie les éléments sous la forme d'une liste 

ligne 141 : Fonction ( mots_score_max ) ==> Cette fonction sert à trouver les mots dont le score tf-idf est le plus élevé. Elle fait cela en parcourant tous les fichiers et retourne tous les mots avec le score tf-idf le plus élevé dans une liste 

ligne 155 : Fonction : ( mot_max_chirac ) ==> Cette fonction parcours le texte des deux discours de Chirac et ressort les mots ayant le score tf-idf le plus élevé dans une liste 

ligne 172 : Fonction ( repetition ) ==> Cette fonction parcours tous les discours et renvoie la liste des présidents qui ont parlé de 'Nation' et renvoie aussi le nom du président qui en a le plus parlé 

ligne 194 : Fonction ( ecologie ) ==> Cette fonction parcours tous les discours et renvoie le nom du président qui a parlé en premmier du climat et/ou d'écologie 

ligne 200 : Fonction ( mots_dans_fichiers ) ==> Cette fonction va prendre tous les mots ayant un score TF-IDF dans chaque fichier et si ce mot ne figure pas dans la liste des mots pas important alors celui ci est ajouté dans une liste qui sera renvoyé en fin de fonction

