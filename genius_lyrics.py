# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

import lyricsgenius as lg

client_access_token = 'GqeDZjpAgJF8OBh69761Ju26cQFz0WuXtI8LkH_vxfnU-CIO-ZqMA4ehIgWeFaKK'

def searchLyric(genius, name, artist):
    return genius.search_song(title=name, artist=artist)

def getLyric(name, artist):
    genius = lg.Genius(client_access_token, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
    searchLyric(genius, name, artist)      

def getLyrics(dico):
    genius = lg.Genius(client_access_token, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
    dico_lyrics = {}
    i = 0
    for k in dico.keys():
        if i == 5:
            return dico 
        else:
            try:
                name = k
                artist = dico[k][0]
                lyric = ""
                lyric += searchLyric(genius, name, artist).lyrics
                dico[k].append(lyric)
                i = i+1
                #print(f"Songs grabbed:{len(song)}")
            except:
                print(f"some exception at {name}: {i}")
    return dico