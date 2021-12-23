# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""
<<<<<<< HEAD

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
    
=======
# Classe mère : Chanson
class Chanson:
    """
    Attributs :
        - Titre (chaîne de caractères)
        - Artiste (liste)
        - Date  (date)
    """
    def __init__(self, titre="", artiste=None, date=""):
        self.titre = titre
        self.artiste = artiste
        self.date = date

# Classe fille : chansons avec paroles en français
class ChansonFR(Chanson):
    def __init__(self, titre="", artiste=None, date="", paroles=""):
        super().__init__(titre=titre, artiste=artiste, date=date)
        self.paroles = paroles
        
    def get_paroles(self):
        return self.paroles
    
# Classe fille : chansons avec paroles en anglais
class ChansonEN(Chanson):
    def __init__(self, titre="", artiste=None, date="", paroles=""):
        super().__init__(titre=titre, artiste=artiste, date=date)
        self.paroles = paroles
        
    def get_paroles(self):
        return self.paroles
>>>>>>> 46dbea2d5e55af8004ab20147ff338b685d3fdfb
