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
    
def noms_president(files_names): # A partir du nom du fichier contenu dans files_names, renvoie le nom du président
    names = []
    for nom in files_names:
        if not fich_to_name(nom) in names:
            names.append(fich_to_name(nom))
    return names

def fich_to_name(nom_f):
    mot = ""
    for char in nom_f[11:]:
        if not char in ".123456789":
            mot += char
        else:
            return mot

def write(name): 
    text = minuscules(name)
    f = open("cleaned/"+name,"w",encoding="utf8")
    for lst in text:
        for mot in lst:
            f.write(mot)
            f.write(" ")
        f.write("\n")
    f.close()
            
def prenom(nom): # Lorsqu'un prenom correspondant a l'une des clé du dictionnaire, renvoie le prénom associé
    prenoms = {"Chirac": "Jacques",
           "Giscard dEstaing": "Valéry",
           "Macron": "Emmanuel",
           "Sarkozy" : "Nicolas",
           "Hollande": "François",
           "Mitterrand": "François"}
    return prenoms[nom]+" "+nom

def fich_to_list(f): # Enleve tous les signes de ponctuation et remplace les ' et - par des espaces
    lst1 = [] 
    for ligne in f:
        mot = ""
        for char in ligne[:-1]:
            if (ord(char) >= 65 and ord(char)<= 90) or (ord(char)>= 191 and ord(char) <= 223):
                char = chr(ord(char)+32)
            if (char <= "z" and char>= "a") or (ord(char)>= 224 and ord(char) <= 255):
                mot+= char
            if char in "'-" and mot != "":
                mot += " "
            if char in ",.;:?! " and mot !="":
                lst1.append(mot)
                mot = ""
    f.close()
    return lst1   
    
def dictionnaire(files_names): # Calcule le nombre d occurence de chaque element d un tableau dans celui ci
    dico = {}
    idx = 0
    for el in files_names:
        f = open("speeches/"+el,"r",encoding="utf8")
        lst = fich_to_list(f)
        dico_temp = dico_of_fich(lst)
        for el in dico_temp:
            if el in dico:
                dico[el].append(dico_temp[el])
            else:
                dico[el] = [0]*idx+ [dico_temp[el]]
        for el in dico:
            if not el in dico_temp:
                dico[el].append(0)
        idx +=1
    return dico           

def dico_of_fich(lst):
    dico= {}
    for el in lst:
        if not el in dico:
            dico[el] = 0
        dico[el] += 1
    return dico
        
def calcul_idf(dico_tf): # Avec le nombre d occurence de chaque mot on calule le log en base 10 de ce mot 
    dico_idf = {}
    for el in dico_tf:
        nbr_fich =0
        for tf in dico_tf[el]:
            if tf != 0:
                nbr_fich +=1
        dico_idf[el] = round(log10(8/nbr_fich),3)
    return dico_idf

def score_tf_idf(files_names):
    dico_tf = dictionnaire(files_names)
    dico_idf = calcul_idf(dico_tf)
    dico_tf_idf = {}
    for el in dico_tf:
        dico_tf_idf[el] = []
        for nbr in dico_tf[el]:
            dico_tf_idf[el].append(nbr*dico_idf[el])
    return dico_tf_idf   
    
def matrice(files_names):
    matrice = {}
    idx = 0
    dico_tf_idf = score_tf_idf(files_names)
    for el in dico_tf_idf:
        if el in matrice:
            matrice[el] += [dico_tf_idf[el]]
        else:
            matrice[el] = dico_tf_idf[el]
        idx+= 1
    return matrice

def mots_pas_imp(matrice): # Parcours chaque mot dans la matrice contenant les discours et si leur score tf-idf=0, le met danns la liste mots_pas_imp
    mots_pas_imp = []
    for el in matrice:
        score_0 = True
        for valeur in matrice[el]:
            if valeur != 0:
                score_0 = False
                break
        if score_0:
            mots_pas_imp.append(el)
    return mots_pas_imp

def mots_score_max(matrice):
    max_val=0
    mots_imp=[]
    for mot in matrice:
        score_tf_idf=matrice[mot]
        score_ttl=score_tf_idf[0]

        if score_ttl>max_val:
            max_val=score_ttl
            mots_imp=[mot]
        elif score_ttl==max_val:
            mots_imp.append(mot)
    return mots_imp

def mot_max_chirac(files_names):
    mot_max_chirac=[]
    ind=0
    for i in files_names:
        f_names=files_names[i]
        if"Chirac" in f_names:
            F=open("speeches/"+ f_names, "r", encoding=="utf8")
            dico_tf_idf=score_tf_idf(F)
            for el in dico_tf_idf:
                if el in mot_max_chirac:
                    mot_max_chirac[el]= mot_max_chirac[el]+[dico_tf_idf[el]]
                else:
                     mot_max_chirac[el]=[]
                     mot_max_chirac[el]= mot_max_chirac[el]+[dico_tf_idf[el]]
            ind=ind+1
        return  mot_max_chirac
        
def repetition(files_names):
    dico_tf = dictionnaire(files_names)
    names,fich = [],[]
    maxi = [0,""]
    for idx in range(len(dico_tf["nation"])):
        el = dico_tf["nation"][idx]
        if el != 0 :
            nom = fich_to_name(files_names[idx])
            fich.append(files_names[idx])
        if not nom in names:
            names.append(nom)
        if maxi[0] < el and nom != maxi[1]:
            maxi =[el, nom]
        if maxi[0] < el and nom == maxi[1]:
            maxi[0] += el
    return names,maxi
                
def ecologie(files_names):
    dico_tf = dictionnaire(files_names)
    for el in dico_tf:
        if el == "climat" or "écologie" in el :
            print(el,dico_tf[el])
            for nbr in range(len(dico_tf[el])):
                if dico_tf[el][nbr] != 0:
                    return prenom(fich_to_name(files_names[nbr]))

def mots_dans_fichiers(files_names):
    mat = matrice(files_names)
    lst = mots_pas_imp(files_names)
    mots_evoq = []
    for el in mat:
        if len(mat[el]) == 8 and not el in lst:
            evoq = True
            for score in mat[el]:
                if score == 0:
                    evoq = False
            if evoq:
                 mots_evoq.append(el)
    return mots_evoq

def question_tokenisee(qst):
    lst_mot = []
    mot = ""
    for char in qst:
        if (ord(char) >= 65 and ord(char)<= 90) or (ord(char)>= 191 and ord(char) <= 223):
            char = chr(ord(char)+32)
        if (char <= "z" and char >= "a") or (ord(char) >= 224 and ord(char) <= 255):
            mot += char
        if char in "'- " and mot != "":
            mot += " "
        if char in ",.;:?! " and mot != "":
            lst_mot.append(mot)
            mot = ""
    if mot != "":
        lst_mot.append(mot)
    return lst_mot

def intersections(files_names,qst):
    lst = question_tokenisee(qst)
    matri = matrice(files_names)
    lst2 = []
    for el in lst:
        if el in matri:
            lst2.append(el)
    return lst2
    
def tf_idf_question(files_names,question):
    mots_qst= intersections(files_names,question)
    occu_mot, dic={},{}
    vecteur_tf_idf_qst=[]
    for mot in mots_qst:
        if mot in occu_mot:
            occu_mot[mot]+=1
        else:    
            occu_mot[mot]=1
        score_idf = calcul_idf(dictionnaire(files_names))[mot]
        score_tf = occu_mot[mot]/len(mots_qst)
        score_tf_idf = round(score_tf*score_idf,4)
        dic[mot] = score_tf_idf
    for mot2 in dictionnaire(files_names):
        if not mot2 in mots_qst:
            vecteur_tf_idf_qst.append(0)
        else:
            vecteur_tf_idf_qst.append(dic[mot2])
    return vecteur_tf_idf_qst

def produit_scalaire(vecteur1,vecteur2):
    produit = 0
    for i in range(len(vecteur1)):
        produit += vecteur1[i]*vecteur2[i]
    return produit

def norme_vecteur(vecteur):
    norme = 0
    for i in range(len(vecteur)):
        norme += vecteur[i]**2
    return sqrt(norme)

def similarité_cos(vecteur1,vecteur2):
    norme = norme_vecteur(vecteur1)*norme_vecteur(vecteur2)
    cos_thêta = produit_scalaire(vecteur1,vecteur2) / norme
    return cos_thêta

def dico_to_matrice(mat):
    mat2 = []
    for idx in range(8):
        mat2.append([])
        for el in mat:
            mat2[idx].append(mat[el][idx])
    return mat2
    
def similarité_doc(files_names,question):
    matrice_question = tf_idf_question(files_names,question)
    matrice_tf_idf = dico_to_matrice(matrice(files_names))
    cos_max =0
    norme_question = norme_vecteur(matrice_question)
    for i in range(8):
        norme_v1 = norme_vecteur(matrice_tf_idf[i])
        if norme_question *norme_v1 == 0:
            cos = 0
        else:
            cos = similarité_cos(matrice_tf_idf[i], matrice_question)
        if cos > cos_max:
            cos_max,idx = cos,i
    return files_names[idx],cos_max

def retrouve_mot(files_names,question):
    f, val = similarité_doc(files_names,question)
    matrice_question = tf_idf_question(files_names,question)
    nbr = 1
    print(max(matrice_question))
    for i in range(len(matrice_question)):
        if matrice_question[i] != 0 :
            nbr +=1
        if matrice_question[i] == max(matrice_question):
            print(matrice_question[i])
            print(nbr)
    return intersections(files_names,question)[nbr]

def liste_mots_doc(files_names):
    lst_fichiers = []
    dico = dictionnaire(files_names)
    for el in dico:
        lst_fichiers.append(el)
    return lst_fichiers
    
def tf_idf_max_qst(files_names, question):
    mot_score_max=""
    mot_tf_idf_max=0
    matrice_question = tf_idf_question(files_names,question)
    for ind in range(len(matrice_question)):
        tf_idf=matrice_question[ind]
        if tf_idf > mot_tf_idf_max:
            mot_tf_idf_max=tf_idf
            mot_score_max= liste_mots_doc(files_names)[ind]
    return mot_score_max

def phrases_of_fich(nom):
    f = open("speeches/"+nom,"r",encoding="utf8")
    phrase,lst = "",[]
    for ligne in f:
        for char in ligne[:-1]:
            if char == ".":
                lst.append(phrase)
                phrase = ""
            elif not char in '"/' :
                phrase+= char
    return lst

def choisir_phrases(files_names,question):
    nom = similarité_doc(files_names,question)
    lst = phrases_of_fich(nom)
    mot = tf_idf_max_qst(files_names, question)
    name_president = prenom(fich_to_name(nom))
    phrases = "" 
    for phr in lst:
        if mot in phr:
            phrases += phr +". "
    return "Comme l'a dit M."+name_president+": \""+ phrases + "\""       
            
# Appels

directory = "speeches"
files_names = list_of_files(directory, "txt")
question =  "Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"

for name in files_names:
    write(name)    

print(choisir_phrases(files_names,question))
