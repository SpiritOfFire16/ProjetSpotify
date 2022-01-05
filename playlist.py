# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

import pickle

class ManagerPlaylist():
    def __init__(self, path):
        self.__path = path
    
    def save(self, playlist):
        with open(self.__path, 'wb') as outp:
            pickle.dump(playlist, outp, pickle.HIGHEST_PROTOCOL)
            print(f"Sauvegarde de la playlist dans le fichier {self.__path}")
            
    def load(self):
        with open(self.__path, 'rb') as inp:
            playlist = pickle.load(inp)
            print(f"Chargement de la playlist depuis le fichier {self.__path}")
        return playlist
    
    def creer_playlist(self, mots_cles, playlist, graphe):
        p = Playlist()
        chansons = playlist.get_chansons()
        for mot in mots_cles:
            if mot in chansons:
                p.add_chanson(chansons[mot])
            else:
                try:
                    titres = graphe.get_titres_chanson(mot)
                    for titre in titres:
                        p.add_chanson(chansons[titre])
                except:
                     print("Erreur noeud inexistant")
        return p


class Playlist():
    
    def __init__(self):
        self.__liste_chansons = {}
        self.__nb_chansons = 0
        
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
        for k,v in self.__liste_chansons.items():
            chansons += str(v) + "\n"
        return f"Nombre de chansons : {self.__nb_chansons}\n{chansons}"