# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

# Pour cette partie, nous nous sommes inspirés des sites disponibles aux adresses suivantes :
# https://pypi.org/project/lyricsgenius/
# https://towardsdatascience.com/song-lyrics-genius-api-dcc2819c29


import lyricsgenius as lg

# Token utilisé pour se connecter à l'api Genius
client_access_token = 'GqeDZjpAgJF8OBh69761Ju26cQFz0WuXtI8LkH_vxfnU-CIO-ZqMA4ehIgWeFaKK'

# Retourne des chansons hébergées sur Genius,
# en fonction d'un titre et d'un nom d'artiste
def searchLyric(genius, name, artist):
    return genius.search_song(title=name, artist=artist)

# Permet de trouver les paroles d'une chanson idisponible sur Genius
# (en fonction de son titre et de son artiste)
def getLyric(name, artist):
    genius = lg.Genius(client_access_token, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
    searchLyric(genius, name, artist)      

# Retourne un dictionnaire contenant les paroles de chansons
def getLyrics(dico):
    genius = lg.Genius(client_access_token, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
    i = 0
    for k in dico.keys():
        if i == 50:
            break
        try:
            name = k
            artist = dico[k][0]
            lyric = ""
            lyric += searchLyric(genius, name, artist).lyrics
            dico[k].append(lyric)
            i = i+1
            #print(f"Songs grabbed:{len(song)}")
        except:
            print(f"some exception at {name}: {k}")
    return dico