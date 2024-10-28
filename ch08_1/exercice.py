#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import os
import json

# TODO: Définissez vos fonction ici
def comparaison(fichier_1, fichier_2):
    with open(fichier_1, encoding = "utf-8") as f1, open(fichier_2, encoding = "utf-8") as f2:
        for count, line1 in enumerate(f1):
            line2 = f2.readline()
            if line1 != line2:
                print(f"The files are not identical. Line {count + 1} is different.")
                print(line1)
                print("Is not the same as:")
                print(line2)
                return
    print("identique")
            
def exercice2(fichier_1, fichier_2):
    with open(fichier_1, encoding = "utf-8") as f1, open(fichier_2, "w", encoding = "utf-8") as f2:
        f2.write(f1.read().replace(" ", "   "))

def exercice3(fichier_1):
    with open(fichier_1, encoding = "utf-8") as f1:
        words = []
        words = f1.read().replace("\n"," ").split(" ")
        deja = {}
        for word in words:
            if word in deja:
                
                deja[word] += 1
            else:
                deja[word] = 1
        print(deja) #reste à trier
                

def exercice_3(fichier_1, intervalle, final):
    with open(fichier_1, "r", encoding= "utf-8") as notes:
        note_percentage = notes.readline()
    with open(intervalle, "r", encoding= "utf-8") as inter:
        equivalence_note = json.load(inter)
    with open(final, "w", encoding= "utf-8") as fin:
        for pourcentage in note_percentage:
            pourcentage_int = int(pourcentage)
            for lettre, intervalle in equivalence_note.items():
                if intervalle[0] <= pourcentage_int < intervalle[1]:
                    fin.write(f"{pourcentage_int} \t {lettre} \n")
                    break
                  
if __name__ == '__main__':
    if not os.path.exists("output"):
        os.mkdir("output")

    # TODO: Appelez vos fonctions ici, mettez vos fichiers de sortie dans le dossier "output".
comparaison("ch08_1/data/exemple.txt", "ch08_1/data/exemple2.txt")

exercice2("ch08_1/data/exemple.txt", "ch08_1/data/exemple2.txt")

exercice3("ch08_1/data/exemple.txt")

exercice_3("ch08_1/data/notes.txt", "ch08_1/data/recettes.json", "ch08_1/data/notesnouv.txt")