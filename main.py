# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

import os
#import pickle

from spotify import getTrack
from genius_lyrics import getLyrics

#cwd = os.getcwd()
#path = cwd + "\\save_Corpus.pkl"
#with open(path, 'wb') as outp:
#    pickle.dump(corpus, outp, pickle.HIGHEST_PROTOCOL)
#    print("\nSauvegarde du corpus dans un fichier")

#with open(path, 'rb') as inp:
#    c = pickle.load(inp)
#    print("Chargement du corpus en mémoire depuis un fichier")





playlist_id_fr = '2IgPkhcHbgQ4s4PdCxljAx'
top_france_2021_fr = getTrack(playlist_id_fr)
#print(top_france_2021_fr)

#playlist_id_en = '37i9dQZF1DXddEJk8r6QZZ'
#top_france_2021_en = getTrack(playlist_id_en)
#print(top_france_2021_en)

dico_lyrics = getLyrics(top_france_2021_fr)
for k,v in dico_lyrics.items():
    try:
        print(f"=> {k}\n{v[2]}\n\n")
    except:
        print(f"Pas de parole pour la chanson {k}")


