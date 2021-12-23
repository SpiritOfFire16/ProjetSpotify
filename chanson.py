# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

class Chanson:
    # Initialisation des variables de la classe
    def __init__(self, titre="", auteur="", date="", url="", paroles=""):
        self.titre = titre
        self.auteur = auteur
        self.date = date
        self.url = url
        self.paroles = paroles

    # Fonction qui renvoie le texte à afficher lorsqu'on tape repr(classe)
    def __repr__(self):
        return f"Titre : {self.titre}\tAuteur : {self.auteur}\tDate : {self.date}\tURL : {self.url}\tParoles : {self.paroles}\t"

    # Fonction qui renvoie le texte à afficher lorsqu'on tape str(classe)
    def __str__(self):
        return f"{self.titre}, par {self.auteur} ({self.date})"

    def getType(self):
        pass
    