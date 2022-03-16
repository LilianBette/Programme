"""
Programme fait par lilian BETTE pour le TP d'algorithmie 1 refait le [09/02/2022]
Entrée 0 [09/02/2022] : Création du programme, exercice et essaie, formatage...
"""
from random import *

def nbChifDec(n):
    if n == 0:
        return 0
    else :
        return 1 + nbChifDec(n//10)

def chiRang(n,k):
    if k == 1 :
        return n-((n//10)*10)
    else:
        return chiRang(n//10,k-1)

def somrang(n): 
    if n<1:   
        return 0
    else :
        return n-((n//10)*10) + somrang(n//10)

def racnum(n):
    if n<10:
        return n
    else :
        return racnum(somrang(n))

def invchif(n):
    #10^nbChifDec *  n-((n//10)*10)
    if n<1:
        return 0
    else :
        return ((10**(nbChifDec(n)-1)) *  (n-((n//10)*10)) + invchif(n//10))
    print(n)

print(invchif(12354))
"""
1 : 
2 : 
3 : 
"""