# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

import os

from spotify import getTrack
from genius_lyrics import getLyrics


from chanson import ChansonGenerator
from playlist import ManagerPlaylist, Playlist

from traitement import Traitement

from graphe import Graphe_Coocurence

def create_playlist(dico_lyrics, langue, nb_chanson_max):
    playlist = Playlist()
    for k,v in dico_lyrics.items():
        if playlist.get_nb_chansons() == nb_chanson_max:
            break
        try:
            chanson_ = ChansonGenerator.factory(langue,k,v[0],v[1],v[2])
            if chanson_ != None:
                playlist.add_chanson(chanson_)
        except:
            print(f"Pas de parole pour la chanson {k}")
    return playlist

def charger_chansons(playlist, maximum):
    playlist_chargee = Playlist()
    i = 0
    for chanson in playlist.get_chansons().values():
        if i == maximum:
            break
        else:
            playlist_chargee.add_chanson(chanson)
            i = i+1
    return playlist_chargee


def main():
    cwd = os.getcwd()
    path_fr = cwd + "\\save_playlist_fr.pkl"
    path_en = cwd + "\\save_playlist_en.pkl"
    manager_fr = ManagerPlaylist(path_fr)
    manager_en = ManagerPlaylist(path_en)
    
    """
    print("==================PLAYLIST FRANCAISE==================")
    #playlist_id_fr = '2IgPkhcHbgQ4s4PdCxljAx'
    playlist_id_fr = '37i9dQZF1DXddEJk8r6QZZ'
    top_france_2021_fr = getTrack(playlist_id_fr)
    dico_2021_lyrics_fr = getLyrics(top_france_2021_fr)
    playlist_2021_fr = create_playlist(dico_2021_lyrics_fr, "en", len(dico_2021_lyrics_fr.keys()))
    manager_fr.save(playlist_2021_fr)
    
    print("==================PLAYLIST ANGLAISE==================")
    playlist_id_en = '2nQ3mO98FmU4wSKtiBU7p5'
    top_france_2021_en = getTrack(playlist_id_en)
    dico_2021_lyrics_en = getLyrics(top_france_2021_en)
    playlist_2021_en = create_playlist(dico_2021_lyrics_en, "en", len(dico_2021_lyrics_en.keys()))
    manager_en.save(playlist_2021_en)
    """
    
    x = 10
    playlist_2021_fr = manager_fr.load()
    playlist_2021_fr_top_x = charger_chansons(playlist_2021_fr, x)
    playlist_2021_en = manager_en.load()
    playlist_2021_en_top_x = charger_chansons(playlist_2021_en, x)
    
    print("\n=====OCCURENCES DES MOTS DANS LES CHANSONS=====")
    print(f"=>TOP {x} des chansons de la PLaylist Française")
    aretes_fr = Traitement.cooccurrences(playlist_2021_fr_top_x)
    print(f"\n\n=>TOP {x} des chansons de la PLaylist Anglaise")
    aretes_en = Traitement.cooccurrences(playlist_2021_en_top_x)
    
    graphe_fr = Graphe_Coocurence(aretes_fr)
    graphe_fr.affichage("chansons_fr.html")
    graphe_en = Graphe_Coocurence(aretes_en)
    graphe_en.affichage("chansons_en.html")
    
if __name__ == "__main__":
    main()


