# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""


import lyricsgenius as lg
import os
from spotify import getTrack

cwd = os.getcwd()
path = cwd + "\\auto_.txt"
file = open(path, "w")

client_access_token = 'GqeDZjpAgJF8OBh69761Ju26cQFz0WuXtI8LkH_vxfnU-CIO-ZqMA4ehIgWeFaKK'
genius = lg.Genius(client_access_token, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

def get_lyrics(arr, k):
    c = 0
    dico_lyrics = {}
    for name in arr:
        try:
            songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
            s = [song.lyrics for song in songs]
            if name in dico_lyrics:
                dico_lyrics[name].append(s)
            else:
                dico_lyrics[name] = s
            #file.write("\n \n   <|endoftext|>   \n \n".join(s))
            c += 1
            print(f"Songs grabbed:{len(s)}")
        except:
            print(f"some exception at {name}: {c}")
    return dico_lyrics

"""
artists = ['Blacks eyed pease', 'Rihanna','Jean Jacques Goldman']
dico_lyrics = get_lyrics(artists, 2)
print(dico_lyrics)
"""

playlist_id_fr = '2IgPkhcHbgQ4s4PdCxljAx'
top_france_2021_fr = getTrack(playlist_id_fr)
print(top_france_2021_fr)

playlist_id_en = '37i9dQZF1DXddEJk8r6QZZ'
top_france_2021_en = getTrack(playlist_id_en)
print(top_france_2021_en)
