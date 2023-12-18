#Main 
#Pour utiliser le programme, veuillez saisir le numéro correspondant à la fonction à laquelle vous voulez accéder
from pychatbot-chabrun-arnoult-d.py import *

if __name__ == '__main__':
    question = input("Quelle est votre question ? ")
    print(choisir_phrases(files_names,question))

