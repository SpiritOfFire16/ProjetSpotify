# -*- coding: utf-8 -*-
"""
@author: ANGUILLA Manon - DAGIER Mathieu

"""

from pyvis.network import Network
import pandas as pd

class Graphe_Coocurence():
    
    def __init__(self, aretes):
        self.__graphe = Network(height='750px', width='100%', bgcolor='#222222', font_color='white')
        self.__graphe.barnes_hut()
        self.__titre_chansons = aretes[aretes.columns[0]]
        self.__mots = aretes[aretes.columns[1]]
        self.__nb_occurences = aretes[aretes.columns[2]]
        self.__aretes = zip(aretes[aretes.columns[0]],aretes[aretes.columns[1]],aretes[aretes.columns[2]])

    def affichage(self, name):
        for a in self.__aretes:
            self.__graphe.add_node(a[0], a[0], title=a[0])
            self.__graphe.add_node(a[1], a[1], title=a[1])
            self.__graphe.add_edge(a[0], a[1], value=a[2])
        voisins_map = self.__graphe.get_adj_list()
        for node in self.__graphe.nodes:
            node['title'] += ' Voisins:<br>' + '<br>'.join(voisins_map[node['id']])
            node['value'] = len(voisins_map[node['id']])
        
        self.__graphe.show(name)