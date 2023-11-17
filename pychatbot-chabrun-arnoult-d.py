# Imports
import os
import math
from math import *

# Fonctions
def list_of_files(directory, extension): # Recupere le nom des fichiers textes contenues dans un dossier
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def minuscules(texte): # Transforme tout les carateres majuscules en minuscules et ecris dans un fichier le meme texte en minuscule
    f = open("cleaned/"+texte,"w",encoding = "utf8")
    text = open("speeches/"+ texte, "r", encoding = "utf8")
    for ligne in text:
        for char in ligne[:-1]:
            if (ord(char) >= 65 and ord(char)<= 90) or (ord(char)>= 191 and ord(char) <= 223):
                char = chr(ord(char)+32)
            f.write(char)
        f.write("\n")
    f.close

def cleaned(f): # Enleve tous les signes de ponctuation et remplace les ' et - par des espaces
    lst1 = [] 
    for ligne in f:
        mot,lst2 = "", []
        for char in ligne[:-1]:
            if char in ",.;:?! " and mot !="":
                lst2.append(mot)
                mot = ""
            elif char in "'-":
                mot += " "
            elif not char in ",.;:?!-' ":
                mot += char
        lst1.append(lst2)
    return lst1      
    
def nom_president(files_names): # A partir du nom du fichier contenu dans files_names, renvoie le nom du président
    names = []
    for nom in files_names:
        mot = ""
        for char in nom[11:]:
            if not char in ".123456789":
                mot += char
            elif char == "." and mot !="":
                if not mot in names:
                    names.append(mot)
                mot = ""
    return names

def prenom(nom): # Lorsqu un prenom correspondant a l une des clé du dictionnaire, renvoie le prénom associé
    prenoms = {"Chirac": "Jacques",
           "Giscard d'Estain": "Valérie",
           "Macron": "Emmanuel",
           "Sarkozy" : "Nicolas",
           "Hollande": "François",
           "Mitterand": "François"}
    return prenoms[nom]

def dictionnaire(lst): # Calcule le nombre d occurence de chaque element d un tableau dans celui ci
    dico = {}
    for el in lst:
        for i in el:
            if i in dico:
                dico[i] += 1
            else:
                dico[i] = 1
    return dico
        
def calcul_tf_idf(dico): # Avec le nombre d occurence de chaque mot on calule le log en base 10 de ce mot 
    for el in dico:
        tf = log(dico[el],10)
        dico[el] = tf
    return dico

def tf_idf_nul(dico): # Lorsque l element est egal a 0 alors la cle est ajoute a une liste
    lst = []
    for el in dico:
        if dico[el] == 0 :
            lst.append(el)
    return lst
    
def passage_en_mini(files_names): # Permet de transformer tous les discours en minuscules
    for el in files_names: # Parcourt les noms de fichier stockées dans files_names 
        minuscules(el) # Appel la fonction minuscule a la ligne 14
        
# Appels

directory = "speeches"
files_names = list_of_files(directory, "txt")
f = open("cleaned/"+files_names[0],"r",encoding = "utf8")

lst = cleaned(f)
dico = dictionnaire(lst)
print(dico)
dico1 = calcul_tf_idf(dico)
print(dico1)
print(tf_idf_nul(dico1))
