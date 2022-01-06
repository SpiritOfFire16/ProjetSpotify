# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

from deep_translator import GoogleTranslator
import re

# Classe ChansonGenerator : permet de gérer l'instanciation des chansons
class ChansonGenerator:
    # Permet de traduire les paroles d'une chanson selon la langue renseignée
    # Nettoyage de certains termes qui sont présents par défault lors de la récupération
    # des paroles depuis Spotify.
    @staticmethod
    def translate(langue, paroles):
        if "🕒" in paroles:
            return None
        elif paroles.count("-") >= len(paroles.split("\n")):
            return None
        elif "feat" in paroles:
            return None
        elif len(paroles.split(" ")) < 100:
            return None
        else:
            paroles = paroles.lower()
            paroles = re.sub("[a-z0-9]*embed[a-z0-9]*","",paroles)
            paroles = re.sub("urlcopopy|off1hare","",paroles)
            return GoogleTranslator(source='auto', target=langue).translate(paroles)
    
    #Permet de créer des ChansonFR et des ChansonEN selon les paramètres renseignés
    @staticmethod
    def factory(langue, titre="", artiste=None, date="", paroles=""):
        if langue == "fr":
            paroles_traduites = ChansonGenerator.translate(langue, paroles)
            if paroles_traduites == None:
                return None
            print("=======Une chanson francaise retournée=======")
            return ChansonFR(titre.upper(), artiste, date, paroles_traduites)
        elif langue == "en":
            paroles_traduites = ChansonGenerator.translate(langue, paroles)
            if paroles_traduites == None:
                return None
            print("=======Une chanson anglaise retournée=======")
            return ChansonEN(titre.upper(), artiste, date, paroles_traduites)
        else:
            assert 0, "Erreur : langue = " + langue


    

# Classe mère : Chanson
class Chanson:
    """
    Attributs privés :
        - Titre (chaîne de caractères)
        - Artiste (liste)
        - Date  (date)
    """
    # Constructeur
    def __init__(self, titre="", artiste=None, date="", paroles=""):
        self.__titre = titre
        self.__artiste = artiste
        self.__date = date
        self.__paroles = paroles
    
    # Retoure le titre de la chanson
    def get_titre(self):
        return self.__titre
    
    # Retoure l'artiste (auteur) de la chanson
    def get_artiste(self):
        return self.__artiste
    
    # Retoure la date de parution de la chanson
    def get_date(self):
        return self.__date
    
    # Retoure les paroles de la chanson
    def get_paroles(self):
        return self.__paroles
    
    # Affichage des informations de la chanson
    def __str__(self):
        return f"Titre : {self.__titre}\nArtiste : {self.__artiste}\nDate de parution : {self.__date}\nParoles : {self.__paroles}\n"


# Classe fille : chansons avec paroles en français
class ChansonFR(Chanson):
    """
    Attributs privés :
        - Titre (chaîne de caractères)
        - Artiste (liste)
        - Date  (date)
        - Paroles (chaîne de caractères)
        - Langue (chaîne de caractères)
    """
    # Constructeur
    def __init__(self, titre="", artiste=None, date="", paroles=""):
        super().__init__(titre=titre, artiste=artiste, date=date, paroles=paroles)
        self.__paroles = paroles
        self.__langue = "FR"
    
    # Retoure les paroles de la chanson
    def get_paroles(self):
        return super().get_paroles()
    
    # Affichage des informations de la chanson
    def __str__(self):
        return f"{super().__str__()}Langue : {self.__langue}\n" 
    
# Classe fille : chansons avec paroles en anglais
class ChansonEN(Chanson):
    """
    Attributs privés :
        - Titre (chaîne de caractères)
        - Artiste (liste)
        - Date  (date)
        - Paroles (chaîne de caractères)
        - Langue (chaîne de caractères)
    """
    # Constructeur
    def __init__(self, titre="", artiste=None, date="", paroles=""):
        super().__init__(titre=titre, artiste=artiste, date=date, paroles=paroles)
        self.__langue = "EN"
        
    # Retoure les paroles de la chanson
    def get_paroles(self):
        return super().get_paroles()
    
    # Affichage des informations de la chanson
    def __str__(self):
        return f"{super().__str__()}Langue : {self.__langue}\n" 
