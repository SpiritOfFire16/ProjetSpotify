# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

import pickle

# Permet de gérer les Playlists
class ManagerPlaylist():
    
    # Constructeur
    def __init__(self, path):
        self.__path = path
    
    # Sauvegarde de la playlist dans un fichier (format pkl)
    def save(self, playlist):
        with open(self.__path, 'wb') as outp:
            pickle.dump(playlist, outp, pickle.HIGHEST_PROTOCOL)
            print(f"Sauvegarde de la playlist dans le fichier {self.__path}")
            
    # Chargement de la playlist depuis un fichier (format pkl)         
    def load(self):
        with open(self.__path, 'rb') as inp:
            playlist = pickle.load(inp)
            print(f"Chargement de la playlist depuis le fichier {self.__path}")
        return playlist
    
    # Création d'une playlist en fonction des mots clés passés en paramètre
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

# Une Playlist est composée de plusieurs chansons, elle permet de les regrouper
class Playlist():
    
    # Constructeur - On initialise avec 0 chanson de base
    def __init__(self):
        self.__liste_chansons = {}
        self.__nb_chansons = 0
        
    # Retourne le nombre de chansons dans la playlist
    def get_nb_chansons(self):
        return self.__nb_chansons
    
    # Retourne une liste de chansons (de la playlist)
    def get_chansons(self):
        return self.__liste_chansons
    
    # Ajoute une chanson dans la playlist
    def add_chanson(self, chanson_a_ajoutee):
        if chanson_a_ajoutee.get_titre() not in self.__liste_chansons:
            self.__liste_chansons[chanson_a_ajoutee.get_titre()] = chanson_a_ajoutee
            self.__nb_chansons = self.__nb_chansons + 1
    
    # Supprime une chanson de la playlist
    def del_chanson(self, chanson_a_supprimee):
        if chanson_a_supprimee.get_titre() in self.__liste_chansons:
            self.__liste_chansons[chanson_a_supprimee.get_titre()].remove()
            self.__nb_chansons = self.__nb_chansons - 1
    
    # Affichage (avec le nombre de chansons)
    def __str__(self):
        chansons = ""
        for k,v in self.__liste_chansons.items():
            chansons += str(v) + "\n"
        return f"Nombre de chansons : {self.__nb_chansons}\n{chansons}"