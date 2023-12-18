# Mathieu Chabrun Quentin Arnoult
#pychatbot-chabrun-arnoult-d

Explication des fonctions du programme : 

Fonction : ( list_of_file )==> Recupere le nom des fichiers contenant les dicsours contenus dans le dossier speeches et le stocke dans la liste files_names

Fonction : ( minuscules ) ==> Cette fonction renvoie une liste de listes, dans laquelle chaquz sous liste contient des mots d'une ligne d'un fichier où les caractères majuscules sont transformés en caractères minuscules et où la pnctuation est effacée. En gros elle réécris les discours en transformant tous les caractères majuscules en minuscules, enlèves les caractères spéciaux ,.;:?!- et stocke dans une liste lst1 tout le texte transformé. 

Fonction : ( nom_president ) ==> En important le nom des fichiers depuis la liste files_names, il nettoie le titre du fichier en enlevant tous les caractères spéciaux ou non de façon a retourner uniquement le nom du président et le stocke dans une liste names

Fonction ( fish_to_name ) ==>  Sous-fonction de nom president. Prend un fichier spécifique et renvoie le nom du président associé au fichier 

Fonction : ( write ) ==> Cette fonction prend un nom de fichier, récupère sa version convertie en minuscule et écrit le contenu converti dans un nouveau fichier dans le dossier "cleaned" avec le même nom qu'il avait avant d'etre transformé

Fonction : ( prenom ) ==> Cette fonction associe, dans un dictionnaire nommé prenom le prénom d'un président à son nom

Fonction : ( fich_to_list ) ==> Cette fonction est presque identique à la fonction minuscule a la seule différence qu'elle remplace les ' et les - par des espaces 

Fonction : ( dictionnaire ) ==> Calcule le nombre d'occurence de chaque mot d'un tableau et le stock dans un dico sous la forme mot : occurence

Fonction : ( dico_to_fish ) ==> Calcule le nombre d'occurrence de chaque mot dans un fichier et stocke le résultat dans un dictionnaire.

Fonction : ( calcul_idf ) ==> Calcule, avec le nombre d'occurence de chaque mot, le log en base 10 de ce motavec la formule idf=og((nombre_total_de_fichiers / nombre_de_fichiers_contenant_le_mot) + 1, 10), arrondis à 3 chiffees après la virgule

Fonction ( score_tf_idf ) ==> Cette fonction utilise le score tf et le score idf. Elle calcule d'abord le score tf dans la matrcie dico_tf. Enfin, elle multiplie le score tf et le score idf pour avoir le score_tf_idf qui représente l'importance de chaque mot dans tous les fichiers  

Fonction ( matrice ) ==> Créer une matrcie et ffiche, comme nombre de lignes le nombre de mots uniques dans tous les fichiers et le nombre de colonnes est égal au nombre de fichiers dans le répertoire

Fonction ( mots_pas_imp ) ==> Cette fonction parcours les éléments de la matrice et a pour but de trouver les mots les - importants, c'est à dire que son score tf_idf=0. Elle renvoie les éléments sous la forme d'une liste 

Fonction ( mots_score_max ) ==> Cette fonction sert à trouver les mots dont le score tf-idf est le plus élevé. Elle fait cela en parcourant tous les fichiers et retourne tous les mots avec le score tf-idf le plus élevé dans une liste 

Fonction : ( mot_max_chirac ) ==> Cette fonction parcours le texte des deux discours de Chirac et ressort les mots ayant le score tf-idf le plus élevé dans une liste 

Fonction ( repetition ) ==> Cette fonction parcours tous les discours et renvoie la liste des présidents qui ont parlé de 'Nation' et renvoie aussi le nom du président qui en a le plus parlé 

Fonction ( ecologie ) ==> Cette fonction parcours tous les discours et renvoie le nom du président qui a parlé en premmier du climat et/ou d'écologie 

Fonction ( mots_dans_fichiers ) ==> Cette fonction va prendre tous les mots ayant un score TF-IDF dans chaque fichier et si ce mot ne figure pas dans la liste des mots pas important alors celui ci est ajouté dans une liste qui sera renvoyé en fin de fonction

Fonction ( question_tokenisee ) ==> Prend une question et retourne une liste de mots en supprimant la ponctuation et en transformant les majuscules en minuscules

Fonction ( intersections ) ==> Prend une liste de fichiers et une question, retourne une liste des mots de la question présents dans la matrice

Fonction ( tf_idf_question ) ==> Calcule le vecteur TF-IDF pour une question donnée par rapport à une liste de fichiers.

Fonction ( pertinence_doc ) ==> Comparaison de la pertinence d'un document par rapport à une question en utilisant la similarité cosinus.

Fonction ( produit_scalaire ) ==> Calcule le produit scalaire entre deux vecteurs

Fonction ( norme_vecteur ) ==> Calcule la norm d'un vecteur 

Fonction ( similarité_cos ) ==> Calcule la similarité cosinus entre deux vecteurs

Fonction ( retrouve_mot ) ==> Convertit un dictionnaire en une matrice.

Fonction ( tf_idf_max_qst ) ==> Identifie le document le plus similaire à la question en calculant la similarité cosinus entre les vecteurs TF-IDF.

Fonction ( phrase_of_fich ) ==> Permet de récupérer chaque phrase d un fichier et de l ajouter comme élément d'une liste

Fonction ( choisir_phrases ) ==> Récupère chaque phrase contenant le mot avec la plus grande similarité et renvoie l ensembke des phrases sur le sujet
