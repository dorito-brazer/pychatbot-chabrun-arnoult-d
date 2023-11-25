# pychatbot-chabrun-arnoult-d

ligne 7 : Fonction : ( list_of_file )==> Recupere le nom des fichiers contenant les dicsours contenus dans le dossier speeches et le stocke dans la liste files_names

ligne 14 : Fonction : ( minuscules ) ==> Cette fonction renvoie une liste de listes, dans laquelle chaquz sous liste contient des mots d'une ligne d'un fichier où les caractères majuscules sont transformés en caractères minuscules et où la pnctuation est effacée. En gros elle réécris les discours en transformant tous les caractères majuscules en minuscules, enlèves les caractères spéciaux ,.;:?!- et stocke dans une liste lst1 tout le texte transformé. 

ligne 33 : Fonction : ( nom_president ) ==> En important le nom des fichiers depuis la liste files_names, il nettoie le titre du fichier en enlevant tous les caractères spéciaux ou non de façon a retourner uniquement le nom du président et le stocke dans une liste names

ligne 46 : Fonction : ( write ) ==> Cette fonction prend un nom de fichier, récupère sa version convertie en minuscule et écrit le contenu converti dans un nouveau fichier dans le dossier "cleaned" avec le même nom qu'il avait avant d'etre transformé

ligne 56 : Fonction : ( prenom ) ==> Cette fonction associe, dans un dictionnaire nommé prenom le prénom d'un président à son nom

ligne 65 : Fonction : ( fich_to_list ) ==> Cette fonction 
