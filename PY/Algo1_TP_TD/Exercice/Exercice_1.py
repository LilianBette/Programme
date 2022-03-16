"""
Programme fait par lilian BETTE pour le TP d'algorithmie 1 refait le [09/02/2022]
Entrée 0 [09/02/2022] : Création du programme, exercice et essaie, formatage...
"""

from random import *

i =0
def binome(n,p):
    global i 
    i=i+1
    if p==0 or p==n :
        return 1
    else :
        return binome(n-1,p)+binome(n-1,p-1)

def binome2(n,p):
    global i
    i = i+1
    if p == 0:
        return 1
    else:
        return (n/p) * binome(n-1,p-1)

def bancEssaie():
    binome(4,8)
    binome2(7,6)

#run
bancEssaie

"""
1 : nombre d'appels [n carré]
2 : ???
3 : implémentation ici.
"""