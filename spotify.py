# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

# Identifiants pour se connecter à l'api de Spotify
cid = "6e40d19100904d7ca8a486798c29a2cd"
csecret = "e23dfd52e41a4eb0b056d7100950960a"

# Retourne une liste d'identifiants de chansons
def getTrackIDs(sp, user, playlist_id):
    track_ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        track_ids.append(track['id'])
    return track_ids

# Retourne un tableau avec les informations suivantes :
# titre, artiste, date de sortie, d'une chanson
def getTrackFeatures(sp, id):
    track_info = sp.track(id)
    name = track_info['name']
    artist = track_info['album']['artists'][0]['name']
    release_date = track_info['album']['release_date']
    track_data = [name, artist, release_date]
    return track_data

# Retourne un dictionnaire contenant toutes les informations d'une playlist (plusieurs chansons)
def getTrack(playlist_id):
    myauth = SpotifyClientCredentials(client_id=cid, client_secret=csecret)
    sp = spotipy.Spotify(auth_manager = myauth)
    track_ids = getTrackIDs(sp, 'spotify', playlist_id)    
    track_dico = {}
    for id_track in track_ids:
        time.sleep(0.3)
        track_data = getTrackFeatures(sp, id_track)
        track_dico[track_data[0]] = track_data[1:]
    return track_dico


