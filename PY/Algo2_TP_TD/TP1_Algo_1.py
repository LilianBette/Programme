"""
Programme fait par lilian BETTE pour le TP d'algorithmie 2 le [24/01/2022]
Entrée 0 [24/01/2022] : Création du programme, exercice et essaie...
"""
from pylab import *

def droit(i):
    """
    Fonction droit
        Cette fonction correspond à la partie droit du tas.
        Argument[1] : i un entier.
        Retour : un entier.
    """
    return 2*i+1

def gauche(i):
    """
    Fonction gauche
        Cette fonction correspond à la partie gauche du tas.
        Argument[1] : i un entier.
        Retour : un entier.
    """
    return 2*i+2

def pere(i):
    """
    Cette fonction correspond à la partie père d'un tas.
        Argument[1] : i un entier.
        Retour : un entier. 
    """
    return (i-1)//2

def verifierProprieteDeTas (t):
    """
    Fonction verifierProprieteDeTas
        Cette fonction permet de vérifier la propriété du tas.
        Argument[1]: t est une liste
        Retour : un booléen.
    """
    for i in range(1,len(t)):
        if t[i] < pere(i):
            return False
    return True
        

def Entasser (t,n,i): 
    """
    Fonction Entasser
        Cette fonction permet d'ajouter des éléments au tas.
        Argument[1]: t une liste, n taille de t, i un entier)
        Retour : 0
    """
    g = gauche(i)
    d = droite(i)
    if g < n and t[g] > t[i] :
        max = g
    else :
        max = i
    if d < n and t[d] > t[max] :
        max = d
    if i != max :
        t[i],t[max] = t[max], t[i]
        Entasser(t,n,max)

def ConstruireTas (t):
    """
    Fonction ConstruireTas
        Cette fonction construit un tas.
        Argument[]:
        Retour :
    """
    for i in range(((n//2)-1),-1,-1):
        Entasser(t,n,i)


def afficherCourbe(L,n):
    plot(array(range(len(L))),array(L),label=n)

def bancEssai():
    for n in range(1,100):

        L=[j for j in range(n)]
        shuffle(L)
        ConstruireTas(L)

def tempsMoyen(fonction,l,n,nbRepetitions=50):
    somme=0
    for k in range(nbRepetitions):
        shuffle(l)
        start=time.time()
        fonction(l,n)
        end=time.time()
        somme+=(end-start)
    return somme/nbRepetitions

#run
t1=[6, 28, 22, 24, 18, 0, 21, 22, 4, 17]
verifierProprieteDeTas(t1)
afficherCourbe(t1,"toto")
show()

