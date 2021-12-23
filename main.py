# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

import os

from spotify import getTrack
from genius_lyrics import getLyrics

cwd = os.getcwd()
path = cwd + "\\auto_.txt"
file = open(path, "w")


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


