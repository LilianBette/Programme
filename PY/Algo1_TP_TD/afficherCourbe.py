from pylab import *
from random import *

def afficherCourbe(maListeDeValeurs):
  plot(array(range(len(maListeDeValeurs))),array(maListeDeValeurs))
  show()

def rechercheSequentielle(liste,x):
  #renvoie un couple a,b où a est un booléen et b est le nombre d'itérations

def bancEssai():
  data=[]
  for i in range(1,1001):
    liste=[randint(0,1000) for _ in range(i)]
    #liste.sort() # dans le cas de la recherche dichotomique
    trouve,nb=rechercheSequentielle(liste,randint(0,1000))
    data.append(nb)
  afficherCourbe(data)

bancEssai()


