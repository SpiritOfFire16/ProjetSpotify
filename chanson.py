# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

from deep_translator import GoogleTranslator

class ChansonGenerator:
    
    @staticmethod
    def translate(langue, paroles):
        if "🕒" in paroles:
            return None
        else:
            return GoogleTranslator(source='auto', target=langue).translate(paroles)

    @staticmethod
    def factory(langue, titre="", artiste=None, date="", paroles=""):
        if langue == "fr":
            paroles_traduites = ChansonGenerator.translate(langue, paroles)
            if paroles_traduites == None:
                return None
            return ChansonFR(titre, artiste, date, paroles_traduites)
        if langue == "en":
            paroles_traduites = ChansonGenerator.translate(langue, paroles)
            if paroles_traduites == None:
                return None
            return ChansonEN(titre, artiste, date, paroles)
        assert 0, "Erreur : langue = " + langue


    

# Classe mère : Chanson
class Chanson:
    """
    Attributs privés :
        - Titre (chaîne de caractères)
        - Artiste (liste)
        - Date  (date)
    """
    def __init__(self, titre="", artiste=None, date=""):
        self.__titre = titre
        self.__artiste = artiste
        self.__date = date
    
    def get_titre(self):
        return self.__titre
    
    def get_artiste(self):
        return self.__artiste
    
    def get_date(self):
        return self.__date
    
    def __str__(self):
        return f"Titre : {self.__titre}\nArtiste : {self.__artiste}\nDate de parution : {self.__date}\n"


# Classe fille : chansons avec paroles en français
class ChansonFR(Chanson):
    def __init__(self, titre="", artiste=None, date="", paroles=""):
        super().__init__(titre=titre, artiste=artiste, date=date)
        self.__paroles = paroles
        
    def get_paroles(self):
        return self.__paroles
    
    def __str__(self):
        return f"{super().__str__()}Langue : FR\n" 
    
# Classe fille : chansons avec paroles en anglais
class ChansonEN(Chanson):
    def __init__(self, titre="", artiste=None, date="", paroles=""):
        super().__init__(titre=titre, artiste=artiste, date=date)
        self.__paroles = paroles
        
    def get_paroles(self):
        return self.__paroles
    
    def __str__(self):
        return f"{super().__str__()}Langue : EN\n" 
