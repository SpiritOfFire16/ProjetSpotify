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

from graphe import Graphe_Cooccurrence

# Création d'une playlist et la retourne
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

# Chargement des chansons d'une playlist, en fonction d'un maximum de chansons déterminé en paramètre
# Retourne la playlist avec le nombre de chansons souhaitées
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

# Affichage textuelle des commandes possibles pour l'utilisateur 
def affichage_regles():
    print("\n\n --------------------------------------------------------------------")
    print("|                              IMPORTANT A LIRE                      |")
    print("--------------------------------------------------------------------\n")
    print("Il existe 6 types de commandes possibles :")
    print("COMMANDE 1 : menu")
    print("Permet d'afficher les informations concernant les différentes commandes réalisables.")
    print("")
    print("COMMANDE 2 : graphe")
    print("Ecrivez : graphe/<langue>/<terme1>...")
    print("Avec : <langue> pouvant prendre les valeurs 'fr' ou 'en'")
    print("Avec : <terme1> pouvant prendre les valeurs suivantes :")
    print(" -> ALL SONGS : afin d'afficher le graphe formé de tous les mots présents dans les chansons de la playlist")
    print(" -> Le titre d'une chanson : afin d'afficher le graphe formé de tous les mots de la chanson")
    print(" -> Un mot : afin d'afficher le graphe formé de tous les mot des chansons qui contiennent le mot choisi")
    print("Remarque : Il est possible d'ajouter plusieurs <termes> les uns à la suite des autres, par exemple on peut ecrire :")
    print(" graphe/en/ALL SONGS/love/hey")
    print("")
    print("COMMANDE 3 : occ")
    print("Ecrivez : occ/<langue>/<terme1>...")
    print("Avec : <langue> pouvant prendre les valeurs 'fr' ou 'en'")
    print("Avec : <terme1> pouvant prendre les valeurs suivantes :")
    print(" -> ALL WORDS : afin d'afficher l'ensemble des mots presents dans la playlist choisie avec les titres des chansons dans lesquels ils apparaissent ainsi que leurs nombres d'occurrences par chanson.")
    print(" -> Un mot : afin d'afficher les titres des chansons dans lesquelles il apparait ainsi que son nombre d'occurences par chanson. ")
    print("Remarque : Il est possible d'ajouter plusieurs <termes> les uns à la suite des autre, par exemple on peut ecrire :")
    print(" occ/fr/many/money/beautiful")
    print("")
    
    print("COMMANDE 4 : sup, inf et supinf")
    print("Ecrivez : sup/<langue>/<nombre>")
    print("Ecrivez : inf/<langue>/<nombre>")
    print("Avec : <langue> pouvant prendre les valeurs 'fr' ou 'en'")
    print("Avec : <nombre> devant prendre les valeurs d'un entier strictement positif")
    print("sup = Cette commande affiche l'ensemble des mots de la playlist choisie dont le nombre d'occurrences est supérieur ou égal au nombre donné par l'utilisateur")
    print("inf = Cette commande affiche l'ensemble des mots de la playlist choisie dont le nombre d'occurrences est inférieur ou égal au nombre donné par l'utilisateur")
    print("Ecrivez : supinf/<langue>/<nombre1>/<nombre2>")
    print("Avec : <nombre1> (borne inférieure) et <nombre2> (borne supérieure) devant prendre les valeurs d'un entier strictement positif")
    print("supinf = Cette commande affiche l'ensemble des mots de la playlist choisie dont le nombre d'occurrences est supérieur ou égal à <nombre1> et est inférieur ou égal à <nombre2> donné par l'utilisateur")
    print("")    
    print("COMMANDE 5 : top")
    print("Ecrivez : top/<langue>/<nombre>")
    print("Avec : <langue> pouvant prendre les valeurs 'fr' ou 'en'")
    print("Avec : <nombre> devant prendre les valeurs d'un entier strictement positif")
    print("Cette commande affiche le top x des mot de la playlist choisie, avec x correspondant à <nombre> donné par l'utilisateur")
    print("")
    print("COMMANDE 6 : -1")
    print("Permet de quitter le programme")

# Création de graphe(s) en fonction des paramètres renseignés
def creation_graphe(mots_cles, graphe, langue, manager, playlist_2021_top_x, couleurs):
    if "ALL SONGS" in mots_cles:
        graphe.affichage("chansons_" + langue + ".html")
        while "ALL SONGS" in mots_cles:
            mots_cles.remove("ALL SONGS")
    if len(mots_cles) > 0:
        playlist = manager.creer_playlist(mots_cles, playlist_2021_top_x, graphe)
        if playlist.get_nb_chansons() > 0:                        
            aretes,correspondances_new = Traitement.cooccurrences(playlist)
            graphe = Graphe_Cooccurrence(aretes, couleurs)
            mots_cles = "_".join(mots_cles)
            graphe.affichage(f"chansons_{mots_cles}.html")
        else:
            print("Erreur mots non trouvés")

# Permet d'indiquer la présence d'un mot dans une ou plusieurs chansons
# ainsi que son nombre total d'occurrences
def nb_occurences_mots(mots_cles, correspondances):
    if len(mots_cles) > 0:
        if "ALL WORDS" in mots_cles:
            for mot in correspondances.columns:
                total = correspondances[mot].sum()
                sous_df = correspondances[correspondances[mot] > 0]
                chansons = sous_df.index
                if len(chansons) == 1 :
                    print(f"Le mot {mot} est contenu dans la chanson :")
                else:
                    print(f"Le mot {mot} est contenu dans les chansons :")
                for titre in chansons:
                    t = titre[len("chanson "):]
                    occ = sous_df.loc[titre][mot]
                    print(f"{t} : {occ} fois ")
                print(f"Nombre total d'occurrences : {total}\n")
            while "ALL WORDS" in mots_cles:
                mots_cles.remove("ALL WORDS")
        
        for mot in mots_cles:
            if mot in correspondances.columns:
                total = correspondances[mot].sum()
                sous_df = correspondances[correspondances[mot] > 0]
                chansons = sous_df.index
                if len(chansons) == 1 :
                    print(f"Le mot {mot} est contenu dans la chanson :")
                else:
                    print(f"Le mot {mot} est contenu dans les chansons :")
                for titre in chansons:
                    t = titre[len("chanson "):]
                    occ = sous_df.loc[titre][mot]
                    print(f"{t} : {occ} fois ")
                print(f"Nombre total d'occurrences : {total}\n")
            else:
                print(f"Le mot {mot} n'est pas contenu dans la playlist")
    else:
        print("Erreur, vous devez specifier un terme")
        
# Permet de rechercher la présence d'un mot et son nombre d'occurrences dans une chanson
# en fonction d'une borne (nombre d'occurrences maximal souhaité)
def inf_mots(mots_cles, correspondances):
    dico = Traitement.tri_mots_croissant(correspondances)
    if len(mots_cles) > 0:
        if len(mots_cles) == 1:
            try:
                maximum = int(mots_cles[0])
                if maximum <= 0:
                    print("Erreur, le nombre maximum d'occurrences doit être un entier supérieur ou égal à 1")
                    return
                cpt = 0
                for k,v in dico.items():
                    if v <= maximum:
                        print(f"{k} : {v} fois")
                        cpt = cpt+1
                    else:
                        break
                if cpt == 0:
                    print("Pas de mot trouvé pour ce nombre maximum d'occurrences")
            except:
                print("Vous devez indiquer un nombre d'occurrences maximum")
        else:
            print("Vous devez seulement indiquer un nombre d'occurrences maximum")
    else:
        print("Vous devez indiquer un nombre d'occurrences maximal à rechercher")

# Permet de rechercher la présence d'un mot et son nombre d'occurrences dans une chanson
# en fonction d'une borne (nombre d'occurrences minimal souhaité)            
def sup_mots(mots_cles, correspondances):
    dico = Traitement.tri_mots_decroissant(correspondances)
    if len(mots_cles) > 0:
        if len(mots_cles) == 1:
            try:
                minimum = int(mots_cles[0])
                if minimum <= 0:
                    print("Erreur, le nombre minimum d'occurrences doit être un entier supérieur ou égal à 1")
                    return
                cpt = 0
                for k,v in dico.items():
                    if v >= minimum:
                        print(f"{k} : {v} fois")
                        cpt = cpt+1
                    else:
                        break
                if cpt == 0:
                    print("Pas de mot trouvé pour ce nombre minimum d'occurrences")
            except:
                print("Vous devez indiquer un nombre d'occurrences minimum")
        else:
            print("Vous devez seulement indiquer un nombre d'occurrences minimum")
    else:
        print("Vous devez indiquer un nombre d'occurrences minimal à rechercher")

# Permet de rechercher la présence d'un mot et son nombre d'occurrences dans une chanson
# entre deux bornes (nombre d'occurrences minimal et maximal souhaité) 
def supinf_mots(mots_cles, correspondances):
    dico = Traitement.tri_mots_croissant(correspondances)
    if len(mots_cles) > 0:
        if len(mots_cles) == 2:
            try:
                if int(mots_cles[0]) <= int(mots_cles[1]):
                    minimum = int(mots_cles[0])
                    maximum = int(mots_cles[1])
                    if minimum <= 0:
                        print("Erreur, le nombre minimum d'occurrences doit être un entier supérieur ou égal à 1")
                        return
                    cpt = 0
                    for k,v in dico.items():
                        if v >= minimum and v <= maximum:
                            print(f"{k} : {v} fois")
                            cpt = cpt+1
                        if v > maximum:
                            break
                    if cpt == 0:
                        print("Pas de mot trouvé pour ces nombres minimum et maximum d'occurrences")
                else:
                    print("Erreur la valeur minimale doit être inférieure ou égale à la valeur maximale")
            except:
                print("Vous devez indiquer un nombre d'occurrences minimum et maximum")
        else:
            print("Vous devez seulement indiquer un nombre d'occurrences minimum et maximum")
    else:
        print("Vous devez indiquer un nombre d'occurrences minimal à rechercher")

# Permet de trouver un top de mots d'une playlist en fonction d'un nombre indiqué 
def top_mots(mots_cles, correspondances):
    dico = Traitement.tri_mots_decroissant(correspondances)
    if len(mots_cles) > 0:
        if len(mots_cles) == 1:
            try:
                top = int(mots_cles[0])
                if top <= 0:
                    print("Erreur, le nombre maximum d'occurrences doit être un entier supérieur ou égal à 1")
                    return
                if top > len(dico.keys()):
                    print("La playlist contient seulement " + str(len(dico.keys())) + " mot(s)")
                cpt = 0
                for k,v in dico.items():
                    if cpt < top:
                        print(f"{k} : {v} fois")
                        cpt = cpt+1
                    else:
                        break
                if cpt == 0:
                    print("Pas de mot trouvé")
            except:
                print("Vous devez indiquer un nombre correspondant au top des mots présents dans la playlist")
        else:
            print("Vous devez seulement indiquer un nombre correspondant au top des mots présents dans la playlist")
    else:
        print("Vous devez indiquer un nombre correspondant au top des mots présents dans la playlist")
       
########################### Lancement du programme principal ###########################
def main():
    
    # Récupération grâces à nos classes Spotipy et Genius des deux playlists utilisées dans le projet
    # Et sauvegarde de ces dernières localement dans deux fichiers (format pkl)
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
    # Stockage des deux playlists avec notre classe ManagerPlaylist
    cwd = os.getcwd()
    path_fr = cwd + "\\save_playlist_fr.pkl"
    path_en = cwd + "\\save_playlist_en.pkl"
    manager_fr = ManagerPlaylist(path_fr)
    manager_en = ManagerPlaylist(path_en)
    
    # Nombre maximum de chansons choisies dans chaque playlist
    # Nous choisissons de prendre les 15 premières chansons de la playlist fr 2021
    # et les 15 premières de la playlist en 2021
    x = 15
    # Chargement des chansons
    playlist_2021_fr = manager_fr.load()
    playlist_2021_fr_top_x = charger_chansons(playlist_2021_fr, x)
    playlist_2021_en = manager_en.load()
    playlist_2021_en_top_x = charger_chansons(playlist_2021_en, x)
    
    # Affiche le nombre d'occurrences des mots dans les chansons pour chacune des playlists
    print("\n=====OCCURRENCES DES MOTS DANS LES CHANSONS=====")
    couleurs_fr = Traitement.choisir_couleurs(playlist_2021_fr_top_x.get_chansons().keys())
    couleurs_en = Traitement.choisir_couleurs(playlist_2021_en_top_x.get_chansons().keys())
    # Affiche le top 15 des chansons de la playlist fr
    print(f"=>TOP {x} des chansons de la Playlist Française")
    aretes_fr,correspondances_fr = Traitement.cooccurrences(playlist_2021_fr_top_x)
    # Affiche le top 15 des chansons de la playlist en
    print(f"\n\n=>TOP {x} des chansons de la Playlist Anglaise")
    aretes_en,correspondances_en = Traitement.cooccurrences(playlist_2021_en_top_x)
    
    # Affecte couleurs aux graphes
    graphe_fr = Graphe_Cooccurrence(aretes_fr, couleurs_fr)
    graphe_en = Graphe_Cooccurrence(aretes_en, couleurs_en)
    
    # Intéractions homme-machine (interface textuelle)
    requete = ""
    while(requete != "-1"):
        requete = input("Entrez le nom d'une commande (ou entrez 'menu' pour en savoir plus) : ")
        if requete != "-1":
            mots_cles = requete.split("/")
            if mots_cles[0] == "graphe":
                if len(mots_cles) > 1:
                    if mots_cles[1] == "fr":
                        creation_graphe(mots_cles[2:], graphe_fr, "fr", manager_fr, playlist_2021_fr_top_x, couleurs_fr)
                    elif mots_cles[1] == "en":
                        creation_graphe(mots_cles[2:], graphe_en, "en", manager_en, playlist_2021_en_top_x, couleurs_en)
                    else:
                        print("Erreur langue non detectée.")
                else:
                    print("Erreur, vous devez spécifier une langue")
            elif mots_cles[0] == "occ":
                if len(mots_cles) > 1:
                    if mots_cles[1] == "fr":
                        nb_occurences_mots(mots_cles[2:], correspondances_fr)
                    elif mots_cles[1] == "en":
                        nb_occurences_mots(mots_cles[2:], correspondances_en)
                    else:
                        print("Erreur langue non detectée.")
                else:
                    print("Erreur, vous devez spécifier une langue")
            elif mots_cles[0] == "inf":
                if len(mots_cles) > 1:
                    if mots_cles[1] == "fr":
                        inf_mots(mots_cles[2:], correspondances_fr)
                    elif mots_cles[1] == "en":
                        inf_mots(mots_cles[2:], correspondances_en)
                    else:
                        print("Erreur langue non detectée.")
                else:
                    print("Erreur, vous devez spécifier une langue")
            elif mots_cles[0] == "sup":
                if len(mots_cles) > 1:
                    if mots_cles[1] == "fr":
                        sup_mots(mots_cles[2:], correspondances_fr)
                    elif mots_cles[1] == "en":
                        sup_mots(mots_cles[2:], correspondances_en)
                    else:
                        print("Erreur langue non detectée.")
                else:
                    print("Erreur, vous devez spécifier une langue")
            elif mots_cles[0] == "supinf":
                if len(mots_cles) > 1:
                    if mots_cles[1] == "fr":
                        supinf_mots(mots_cles[2:], correspondances_fr)
                    elif mots_cles[1] == "en":
                        supinf_mots(mots_cles[2:], correspondances_en)
                    else:
                        print("Erreur langue non detectée.")
                else:
                    print("Erreur, vous devez spécifier une langue")
            elif mots_cles[0] == "top":
                if len(mots_cles) > 1:
                    if mots_cles[1] == "fr":
                        top_mots(mots_cles[2:], correspondances_fr)
                    elif mots_cles[1] == "en":
                        top_mots(mots_cles[2:], correspondances_en)
                    else:
                        print("Erreur langue non detectée.")
                else:
                    print("Erreur, vous devez spécifier une langue")
            elif mots_cles[0] == "menu":
                affichage_regles()
            else:
                print("Erreur commande non detectée.")
        else:
            print("Programme terminé.")
    
if __name__ == "__main__":
    main()


