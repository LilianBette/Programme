"""
Programme fait par lilian BETTE pour le TP d'algorithmie 4 fait le [07/03/2022]
Entrée 0 [07/03/2022] : Création du programme, exercice et essaie, formatage...
"""
import networkx as nx
import matplotlib.pyplot as plt
import pylab
G=nx.generators.random_graphs.fast_gnp_random_graph(10,1/6)
nx.draw(G,with_labels=True, font_weight='bold')
plt.show()
import time
numComp = [i for i in range(100)]

def composantesConnexes(e,n):
    """
    Méthode composantesConnexes
        Cette méthode renvoie ...
        Argument [2] : E : e liste , n entier.
        Valeur de retour : tableau d'entier.
    """
    numComp = [i for i in range(n)]
    for j in e :
        print(j)
        x=j[0]
        y=j[1]
        if numComp[x] != numComp[y]:
            save = numComp[x]
            for i in range(n):
                if numComp[i] == save:
                    numComp[i] = numComp[y]
    return numComp

print('Début composantesConnexes.')
print (composantesConnexes(G.edges , G.number_of_nodes()))
print('Fin composantesConnexes.')


def composantesConnexesOptimisées (e, n):
    """
    Méthode composantesConnexesOptimisées
        Cette méthode renvoie ...
        Argument [2] : ...
        Valeur de retour : tableau d'entier.
    """
    for i in range (n-1):
        numComp = [i for i in range(n)]
        numComp[i] = i
        L = []
        (L[numComp[i]].append,i) 
        taille = [numComp[i]] = 1
    for j in range (e) :
        if numComp[x] != numComp[y]:
            if taille[numcomp[x]] > taille[numComp[y]] :
                x,y = y,x
            save = numComp[x]
            taille[numComp[y]] = taille[numComp[y]]+taille[numComp[x]]
            while not estVide(l[save]) :
                sommet = (L.pop[save])
                numComp[sommet == numComp[y]]
                (L[numComp[y]].append,sommet)
    return numComp


def afficherCourbe(maListeDeValeurs,name):
  pylab.plot(pylab.array(range(len(numComp))),pylab.array(numComp),label=nom)
  pylab.legend(loc='upper right')
  pylab.show()
  
def tempsMoyen(fonction,E,n,nbRepetitions):
  start=time.time()
  for k in range(nbRepetitions):
    fonction(E,n)
  end=time.time()
  return (end-start)/nbRepetitions

print('Début composantesConnexesOptimisées.')
print (composantesConnexesOptimisées(G.edges , G.number_of_nodes()))
print('Fin composantesConnexesOptimisées.')
print(tempsMoyen(composantesConnexesOptimisées,G.edges , G.number_of_nodes(),50))
