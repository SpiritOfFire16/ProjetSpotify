# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

import string
import re

import pandas as pd

import random
from couleur import Couleur

# Classe Traitement
class Traitement():
    # Permet de nettoyer une chaîne de caractères
    # Passage de la chaîne de caractères en minuscule
    # Suppression des mots de liaisons
    # Suppression de la ponctuation
    @staticmethod
    def nettoyage(chaine):
        chaine = chaine.lower()
        words = re.findall("\w+",chaine)
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in words]
        
        stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']
        stripped = [w for w in stripped if w not in stop_words]
        return stripped

    # Permet de créer un dictionnaire formé de : titre de chanson (clé) - couleur (valeur)
    # Avec chaque couleur différente et tirée aléatoirement
    @staticmethod
    def choisir_couleurs(titres):
        randomlist = []
        titres_couleurs = {}
        for t in titres:
            t = t.upper()
            n = random.randint(1,Couleur.get_nb_couleurs())
            while n in randomlist:
                n = random.randint(1, Couleur.get_nb_couleurs())
            randomlist.append(n)
            titres_couleurs[t] = Couleur.get_couleur(n)
        return titres_couleurs

    # Permet de générer les arêtes du futur graphe (sous forme de DataFrame)
    # Permet de créer le DataFrame contenant en colonne les mots de la playlist,
    # en index les titres des chansons et pour chaque intersection : le nombre
    # d'occurrences du mot dans la chanson
    @staticmethod
    def cooccurrences(playlist):
        occurrences_mots = {}
        titres = set()
        for titre,chanson in playlist.get_chansons().items():
            titre = titre.upper()
            titres.add(titre)
            paroles = chanson.get_paroles()
            paroles = Traitement.nettoyage(paroles)
            for mot in paroles:
                if mot not in occurrences_mots:
                    occurrences_mots[mot] = {titre:1}
                else:
                    if titre not in occurrences_mots[mot]:
                        occurrences_mots[mot][titre] = 1
                    else:
                        occurrences_mots[mot][titre] = occurrences_mots[mot][titre]+1
        
        correspondances = pd.DataFrame(0, columns = occurrences_mots.keys(), index = ["chanson " + x for x in list(titres)])
        aretes = pd.DataFrame(columns=["Titre_chanson","Mot","Nb_occurrences"])
        for mot,dico in occurrences_mots.items():
            for titre,nb_occurrence in dico.items():
                correspondances.loc["chanson " + titre, mot] = nb_occurrence
                aretes = aretes.append({"Titre_chanson":titre,"Mot":mot,"Nb_occurrences":nb_occurrence}, ignore_index=True)
        print(correspondances)
        return aretes,correspondances
    
    # Permet de créer un dictionnaire formé des : mots (clé) et de leur nombre
    # d'occurrences dans toute la playlist (valeur) trié par ordre croissant des valeurs
    @staticmethod
    def tri_mots_croissant(df):
        occurrence = {}
        for c in df.columns:
            occurrence[c] = df[c].sum()
        dico_tri = {k: v for k, v in sorted(occurrence.items(), key=lambda item: item[1])}
        return dico_tri            
 
    # Permet de créer un dictionnaire formé des : mots (clé) et de leur nombre
    # d'occurrences dans toute la playlist (valeur) trié par ordre décroissant des valeurs
    @staticmethod
    def tri_mots_decroissant(df):
        occurrence = {}
        for c in df.columns:
            occurrence[c] = df[c].sum()
        dico_tri = {k: v for k, v in sorted(occurrence.items(), key=lambda item: item[1], reverse=True)}
        return dico_tri
            
