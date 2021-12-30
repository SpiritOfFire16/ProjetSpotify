# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

import string
import re

import pandas as pd

class Traitement():
    
    @staticmethod
    def nettoyage(chaine):
        chaine = chaine.lower()
        words = re.findall("\w+",chaine)
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in words]
        
        stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']
        stripped = [w for w in stripped if w not in stop_words]
        #chaine = " ".join(stripped)
        
        return stripped

    @staticmethod
    def cooccurrences(playlist):
        occurrences_mots = {}
        titres = set()
        for titre,chanson in playlist.get_chansons().items():
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
        aretes = pd.DataFrame(columns=["Titre_chanson","Mot","Nb_occurences"])
        for mot,dico in occurrences_mots.items():
            for titre,nb_occurrence in dico.items():
                correspondances.loc["chanson " + titre, mot] = nb_occurrence
                aretes = aretes.append({"Titre_chanson":titre,"Mot":mot,"Nb_occurences":nb_occurrence}, ignore_index=True)
        #print(len(occurrences_mots.keys()))
        print(correspondances)
        return aretes
        
            
