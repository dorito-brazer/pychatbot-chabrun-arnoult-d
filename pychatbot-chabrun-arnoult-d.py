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
    text = open("speeches/"+ texte, "r", encoding = "utf8")
    lst1 = [] 
    for ligne in text:
        mot,lst2 = "", []
        for char in ligne[:-1]:
            if (ord(char) >= 65 and ord(char)<= 90) or (ord(char)>= 191 and ord(char) <= 223):
                char = chr(ord(char)+32)
            if (char <= "z" and char>= "a") or (ord(char)>= 224 and ord(char) <= 255):
                mot+= char
            if char in "'- " and mot != "":
                mot += " "
            if char in ",.;:?!" and mot !="":
                lst2.append(mot)
                mot = ""
        lst1.append(lst2)
    text.close()
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

def write(name):
    text = minuscules(name)
    f = open("cleaned/"+name,"w",encoding="utf8")
    for lst in text:
        for mot in lst:
            f.write(mot)
            f.write(" ")
        f.write("\n")
            
            
def prenom(nom): # Lorsqu un prenom correspondant a l une des clé du dictionnaire, renvoie le prénom associé
    prenoms = {"Chirac": "Jacques",
           "Giscard dEstaing": "Valéry",
           "Macron": "Emmanuel",
           "Sarkozy" : "Nicolas",
           "Hollande": "François",
           "Mitterrand": "François"}
    return prenoms[nom]

def fich_to_list(f): # Enleve tous les signes de ponctuation et remplace les ' et - par des espaces
    lst1 = [] 
    for ligne in f:
        mot,lst2 = "", []
        for char in ligne[:-1]:
            if char == " " and mot !="":
                lst2.append(mot)
                mot = ""
            elif not char in ",.;:?!-' ":
                mot += char
        lst1.append(lst2)
    return lst1     
    
def dictionnaire(lst): # Calcule le nombre d occurence de chaque element d un tableau dans celui ci
    dico = {}
    for el in lst:
        for i in el:
            if i in dico:
                dico[i] += 1
            else:
                dico[i] = 1
    return dico
        
def calcul_idf(dico_tf): # Avec le nombre d occurence de chaque mot on calule le log en base 10 de ce mot 
    dico_idf = {}
    for el in dico_tf:
        idf = log(1/dico_tf[el],10)
        dico_idf[el] = idf
    return dico_idf

def score_tf_idf(dico_tf,dico_idf):
    dico_tf_idf = {}
    for el in dico_tf:
        dico_tf_idf[el] = dico_tf[el]*dico_idf[el]
    return dico_tf_idf    

def tf_idf_nul(dico): # Lorsque l element est egal a 0 alors la cle est ajoute a une liste "nul"
    nul = []
    for el in dico:
        if dico[el] == 0 :
            nul.append(el)
    return nul
    
def matrice(files_names):
    for i in range(len(files_names)):
        f_names = files_names[i]
        f = open("cleaned/"+f_names,"r",encoding= "utf8")


def matrice_resultante_tf_idf():
    for el1 in range(nul):
        LST=[]
        for j in range(len(files_names)):
            f_names = files_names[i]
            f = open("cleaned/"+f_names,"r",encoding= "utf8")

def matrice_res(files_names):
    contenu_fich=[]
    ind=0
    for i in range(len(files_names)):
        with open("cleaned/"+f_names, "r", encoding="utf8") as fich:
            élément=fich.read
            contenu_fich=.append(contenu)
        ind+=1
    matr_res=[]
    for fich in range(len(contenu_fich)):
       ligne=[]
        for i in range 
        
        
            
        
            
            
            
        
        
    
        
        
        
        
# Appels

directory = "speeches"
files_names = list_of_files(directory, "txt")
lst = []
#for name in files_names:
#    write(name)

f = open("cleaned/"+ files_names[0], "r",encoding="utf8")
lst = fich_to_list(f)

dico_tf = dictionnaire(lst)
print(dico_tf)
dico_idf = calcul_idf(dico_tf)
dico_tf_idf = score_tf_idf(dico_tf,dico_idf)
print(dico_idf)
print(dico_tf_idf)
print(tf_idf_nul(dico_tf_idf))
