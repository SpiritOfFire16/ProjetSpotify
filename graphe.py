# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

from pyvis.network import Network

# Permet de créer et afficher un graphe
class Graphe_Coocurence():
    
    # Permet de créer le graphe : ajoute les noeuds, ajoute les arêtes, ajoute le nombre de voisins d'un noeud
    def preparation(self):
        for a in self.__aretes:
            self.__graphe.add_node(a[0], a[0], title="Type: Noeud<br>Titre: "+a[0], color=self.__couleurs[a[0]])
            self.__graphe.add_node(a[1], a[1], title="Type: Noeud<br>Mot: "+a[1], color="white")
            self.__graphe.add_edge(a[0], a[1], title="Type: Arc<br>Titre: "+a[0]+"<br>Mot: "+a[1]+"<br>Poids: "+str(a[2]), value=a[2])
        voisins_map = self.__graphe.get_adj_list()
        for node in self.__graphe.nodes:
            nb_voisins = len(voisins_map[node['id']])
            node['title'] += '<br>Nombre de voisins: '+ str(nb_voisins)
            node['value'] = nb_voisins
    
    # Constructeur du graphe
    def __init__(self, aretes, couleurs):
        self.__graphe = Network(height='750px', width='100%', bgcolor='#222222', font_color='white')
        self.__graphe.barnes_hut()
        self.__titre_chansons = aretes[aretes.columns[0]]
        self.__mots = aretes[aretes.columns[1]]
        self.__nb_occurences = aretes[aretes.columns[2]]
        self.__aretes = zip(aretes[aretes.columns[0]],aretes[aretes.columns[1]],aretes[aretes.columns[2]])
        self.__couleurs = couleurs
        self.preparation()
    
    # Affichage 
    def affichage(self, name):
        self.__graphe.show(name)
        
        
    # Retourne les titres de chansons d'un noeud ciblé
    def get_titres_chanson(self, id_noeud):
        id_noeud = id_noeud.lower()
        voisins_map = self.__graphe.get_adj_list()
        noeud = self.__graphe.get_node(id_noeud)
        return voisins_map[noeud["id"]]
        
        
        
        
        
        
        