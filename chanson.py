# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

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
