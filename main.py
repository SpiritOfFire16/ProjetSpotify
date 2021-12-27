# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

import os

from spotify import getTrack
from genius_lyrics import getLyrics


"""
from deep_translator import GoogleTranslator
import string
import re

def nettoyer_texte(chaine):
    if "🕒" in chaine:
        return None
    chaine = GoogleTranslator(source='auto', target='en').translate(chaine)
    chaine = chaine.lower()
    chaine = re.sub("[a-z0-9]*embed[a-z0-9]*","",chaine)
    chaine = re.sub("urlcopopy|off1hare","",chaine)
    words = re.findall("\w+",chaine)
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in words]
    stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']
    stripped = [w for w in stripped if w not in stop_words]
    chaine = " ".join(stripped)
    #chaine = " ".join(stripped)
    #chaine = GoogleTranslator(source='auto', target='fr').translate(chaine)    
    #return chaine
    return chaine
"""

from chanson import ChansonGenerator
from playlist import ManagerPlaylist, Playlist

import sys

def create_playlist(dico_lyrics, langue, nb_chanson_max):
    playlist = Playlist()
    for k,v in dico_lyrics.items():
        if playlist.get_nb_chansons() == nb_chanson_max:
            break
        try:
            chanson_ = ChansonGenerator.factory(langue,k,v[0],v[1],v[2])
            print(chanson_)
            if chanson_ != None:
                playlist.add_chanson(chanson_)
        except:
           print(f"Pas de parole pour la chanson {k}")
    return playlist


def main():
    cwd = os.getcwd()
    path_fr = cwd + "\\save_playlist_fr.pkl"
    path_en = cwd + "\\save_playlist_en.pkl"
    
    print("==================PLAYLIST FRANCAISE==================")
    #playlist_id_fr = '2IgPkhcHbgQ4s4PdCxljAx'
    playlist_id_fr = '37i9dQZF1DXddEJk8r6QZZ'
    top_france_2021_fr = getTrack(playlist_id_fr)
    dico_2021_lyrics_fr = getLyrics(top_france_2021_fr)
    playlist_2021_fr = create_playlist(dico_2021_lyrics_fr, "fr", 2)
    manager_fr = ManagerPlaylist(path_fr)
    manager_fr.save(playlist_2021_fr)
    
    print("==================PLAYLIST ANGLAISE==================")
    playlist_id_en = '2nQ3mO98FmU4wSKtiBU7p5'
    top_france_2021_en = getTrack(playlist_id_en)
    dico_2021_lyrics_en = getLyrics(top_france_2021_en)
    playlist_2021_en = create_playlist(dico_2021_lyrics_en, "en", 2)
    manager_en = ManagerPlaylist(path_en)
    manager_en.save(playlist_2021_en)
    

    
if __name__ == "__main__":
    main()


