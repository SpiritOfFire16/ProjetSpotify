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



playlist_id_fr = '2IgPkhcHbgQ4s4PdCxljAx'
top_france_2021_fr = getTrack(playlist_id_fr)
#print(top_france_2021_fr)

#playlist_id_en = '37i9dQZF1DXddEJk8r6QZZ'
#top_france_2021_en = getTrack(playlist_id_en)
#print(top_france_2021_en)




from chanson import ChansonGenerator,Chanson,ChansonFR,ChansonEN
from playlist import Playlist
import sys

dico_lyrics = getLyrics(top_france_2021_fr)
playlist_2021_fr = Playlist()

for k,v in dico_lyrics.items():
    if playlist_2021_fr.get_nb_chansons() == 20:
        break
    try:
        #print(nettoyer_texte(v[2]))
        chanson_fr = ChansonGenerator.factory("fr",k,v[0],v[1],v[2])
        if chanson_fr != None:
            playlist_2021_fr.add_chanson(chanson_fr)
    except:
        print("Erreur : " + sys.exc_info()[0])
        print(f"Pas de parole pour la chanson {k}")
        
print(playlist_2021_fr)

