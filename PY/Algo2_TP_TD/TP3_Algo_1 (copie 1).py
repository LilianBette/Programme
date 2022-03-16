"""
Programme fait par lilian BETTE pour le TP d'algorithmie 2 fait le [14/02/2022]
Entrée 0 [14/02/2022] : Création du programme, exercice et essaie, formatage...
"""
import networkx as nx
import matplotlib.pyplot as plt
from pylab import *

class ABR :
    def __init__(self,racine=None):
        if racine is not None:
            self.racine=racine
        else:
            self.racine=None

class Sommet :
    def __init__(self,clef=None):
        self.pere=None
        self.gauche=None
        self.droit=None
        if clef is not None:
            self.clef=clef
        else:
            self.clef=None

    def estVide (self):
        """
        Méthode estVide
            Cette méthode renvoi True ou False si l'arbre est vide ou non.
                Argument [0] : Aucun.
                Valeur de retour : Un boléen.
        """
        return False

    #def getClef():
        #return self.clef

    
def inserer(T,z):
    """
    Méthode Inserer
        Cette méthode insère le sommet z à l'arbre T.
            Argument [2] : T une liste, z un entier.
            Valeur de retour :
    """
    y = None
    x = T.racine
    while x is not None : 
        y = x
        if z.clef < x.clef :
            x = x.gauche
        else:
            x = x.droit
    z.pere = y
    if y is None :
        T.racine = z
    else:
        if z.clef < y.clef:
            y.gauche = z
        else:
            y.droit = z

def genererArbre(n):
    """
    Méthode genererArbre
        Cette méthode renvoi un arbre à n sommet.
            Argument [1] : N un entier.
            Valeur de retour : ABR  à n sommets.
    """ 
    A=ABR()                                      
    l = [i for i in range (n)]
    shuffle(l)
    for i in l:
        inserer(A,Sommet(i))
    return A

def afficher(T):
    G = nx.DiGraph()
    def construireGraphe(x,G):
        if x is not None:
            G.add_node(x.clef)
            if x.gauche is not None :
                G.add_edge(x.clef,x.gauche.clef,gd='red')
                construireGraphe(x.gauche,G)
            if x.droit is not None :
                G.add_edge(x.clef,x.droit.clef,gd='blue')
                construireGraphe(x.droit,G) 
    construireGraphe(T.racine,G)
    attr=nx.get_edge_attributes(G,'gd')
    colorsOfEdges=[c for  e,c in attr.items()]
    colorsOfVertices=['yellow']+['blue']*(G.number_of_nodes()-1)
    nx.draw_planar(G,with_labels = True,edge_color=colorsOfEdges,node_color=colorsOfVertices) 
    pos=nx.planar_layout(G) 
    labelsOfEdges=dict([((u,v,),'gauche' if d['gd']=='red' else 'droit') for u,v,d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labelsOfEdges)
    print("racine de l'arbre :",T.racine.clef)
    plt.show()

def parcoursInfixe(x):
    if x is not None :
        parcoursInfixe(x.gauche)
        print(x.clef)
        parcoursInfixe(x.droit)

def rechercherRec(x,k):
    if x == None or x.clef == k :
        return x
    if k < x.clef :
        return rechercher(x.gauche, k)
    else :
        return rechercher(x.droit, k)

def rechercherIt(x,k):
    while x is not None and k is not x.clef :
        if k < x.clef :
            x = x.gauche
        else :
            x = x.droit
        return x

def minimum(x):
    while x.gauche is not None :
        x = x.gauche
    return x

def maximum(x):
    while x.droit is not None :
        x = x.droit
    return x

def successeur(x):
    if x.droit is not None :
        return min(x.droit)
    else :
        y = x.pere
        while y is not None and x == y.droit :
            x = y
            y = y.pere
        return y

def predecesseur(x):
    if x.gauche is not None : 
        return min(x.droit)
    else :
        y = x.pere
        while y is not None and x == y.droit :
            x = y
            y = y.pere
        return y

def suppresion(T,z):
    if z.gauche == None or z.droit == None :
        y = z
    else :
        y = z.successeur
    if y.gauche is not None :
        x = y.gauche
    else:
        x = y.droit
    if y.pere == None :
        T.racine = x
    else :
        if y == y.pere.gauche :
            y.pere.gauche = x
        else :
            y.pere.droit = x
    if y != z :
        z.clef = y.clef
    return y

T=genererArbre(10)
afficher(T)
parcoursInfixe(T.racine)
print(rechercherIt(T.racine, 4))
print(rechercherRec(T.racine, 4))
minimum(T.racine)
maximum(T.racine)
successeur(T.racine)
predecesseur(T.racine)
suppresion(T.racine, )