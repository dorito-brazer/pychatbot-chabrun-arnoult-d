#Main 
#Pour utiliser le programme, veuillez saisir le numéro correspondant à la fonction à laquelle vous voulez accéder
from pychatbot-chabrun-arnoult-d.py import *

if __name__ == '__main__':
    Fonction = int(input("Saisir le numéro de la fonctionnalité: "))
    if Fonction == 1 :
      mots_pas_imp(matrcie)
    elif Fonction == 2:
        mots_score_max(matrice)
    elif Fonction == 3 :
        mot_max_chirac(files_names)
    elif Fonction == 4 :
        repetition(files_names)
    elif Fonction == 5 :
        ecologie(files_names)
    elif Fonction == 6 :
        fct3()  
    else:
        print("Ce numéro de fonction n'existe pas")
      
