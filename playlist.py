# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

from chanson import Chanson

class Playlist():
    
    def __init__(self, liste_chansons={}):
        self.__liste_chansons = liste_chansons
        self.__nb_chansons = len(liste_chansons)
        
    def get_nb_chansons(self):
        return self.__nb_chansons
    
    def get_chansons(self):
        return self.__liste_chansons
    
    def add_chanson(self, chanson_a_ajoutee):
        if chanson_a_ajoutee.get_titre() not in self.__liste_chansons:
            self.__liste_chansons[chanson_a_ajoutee.get_titre()] = chanson_a_ajoutee
            self.__nb_chansons = self.__nb_chansons + 1

    def del_chanson(self, chanson_a_supprimee):
        if chanson_a_supprimee.get_titre() in self.__liste_chansons:
            self.__liste_chansons[chanson_a_supprimee.get_titre()].remove()
            self.__nb_chansons = self.__nb_chansons - 1
            
    def __str__(self):
        chansons = ""
        for k in self.__liste_chansons.keys():
            chansons += "- " + k + "\n"
        return f"Nombre de chansons : {self.__nb_chansons}\n{chansons}"