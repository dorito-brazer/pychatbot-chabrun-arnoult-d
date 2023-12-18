#Main 
#Pour utiliser le programme, veuillez saisir le numéro correspondant à la fonction à laquelle vous voulez accéder
from pychatbot-chabrun-arnoult-d.py import *

if __name__ == '__main__':
    chat = input("Voulez vous accéder au Chatbot ? (oui/non) ")
    if chat == "oui" :
        question = input("Quelle est votre question ? ")
        print(choisir_phrases(files_names,question))
    fonctionnalité = input("Voulez-vous utiliser une des fonctionnalités ? (oui/non) ")
    while fonctionnalité == "oui":                   
        Fonction = int(input("""Saisir le numéro de la fonctionnalité: 
1. Quels sont les mots non importants ?
2. Quel est le mot avec le score maximal ?
3. Quel est le mot le plus répété par Chirac ?
4. Qui parle de Nation et qui l evoque le plus ?
5. Qui est le premier président a parler de climat ?
6. Quels sont les mots dits par tout les presidents tout en étant important ?
"""))
        if Fonction == 1 :
            print(mots_pas_imp(files_names))
        elif Fonction == 2:
            print(mots_score_max(files_names))
        elif Fonction == 3 :
            print(mot_max_chirac(files_names))
        elif Fonction == 4 :
            print(repetition(files_names))
        elif Fonction == 5 :
            print(ecologie(files_names))
        elif Fonction == 6 :
            print(mots_dans_fichiers(files_names))
        else:
            print("Ce numéro de fonction n'existe pas")
        fonctionnalité = input("Voulez-vous utiliser une des fonctionnalités ? (oui/non) ")
