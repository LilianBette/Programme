"""
Programme fait par lilian BETTE pour le TP d'algorithmie 2 fait le [24/01/2022]
Entrée 0 [24/01/2022] : Création du programme, exercice et essaie, formatage...
Entrée 1 [31/01/2022] : Continuation, essaie et correction, fonctionnel.
"""
from pylab import *
from random import *

nB = 0

def droite(i):
    """
    Fonction droite
        Cette fonction correspond à la partie droit du tas.
        Argument[1] : E: i: entier.
        Retour : un entier.
    """
    return 2*i+1

def gauche(i):
    """
    Fonction gauche
        Cette fonction correspond à la partie gauche du tas.
        Argument[1] : E : i: entier.
        Retour : un entier.
    """
    return 2*i+2

def pere(i):
    """
    Cette fonction correspond à la partie père d'un tas.
        Argument[1] : E: i : entier.
        Retour : un entier. 
    """
    return (i-1)//2

def verifierProprieteDeTas (tab):
    """
    Fonction verifierProprieteDeTas
        Cette fonction permet de vérifier la propriété du tas.
        Argument[1]: ES : tab : tableau d'entiers.
        Retour : booléen.
    """
    for i in range(1,len(tab)):
        if tab[i] < pere(i):
            return False
    return True
        

def Entasser (tab,n,i): 
    global nB
    nB+=1
    """
    Fonction Entasser
        Cette fonction permet d'ajouter des éléments au tas.
        Argument[3]: ES tab: tableau d'entiers, n: entier, i: entier)
        Retour : 0
    """
    g = gauche(i)
    d = droite(i)
    if g < n and tab[g] > tab[i] :
        max = g
    else :
        max = i
    if d < n and tab[d] > tab[max] :
        max = d
    if i != max :
        tab[i],tab[max] = tab[max], tab[i]
        Entasser(tab,n,max)

def ConstruireTas (tab,n):
    """
    Fonction ConstruireTas
        Cette fonction construit un tas.
        Argument[2]:ES: tab:tableau d'entiers, E: n:entier
        Retour : 0
    """
    for i in range(((n//2)-1),-1,-1):
        Entasser(tab,n,i)

def TrierParTas (tab,n):
    """
    Fonction ConstruireTas
        Cette fonction construit un tas.
        Argument[2]:ES T:tableau d'entiers,E n:entier.
        Retour : 0
    """
    ConstruireTas(tab,n)
    for i in range (len(tab)-1,-1,-1):
        tab[0],tab[i] = tab[i],tab[0]
        Entasser(tab,i,0)

def max(tab,n):
    return tab[0]

def extraireMax(tab):
    if len(tab)<= 0:
        print("Erreur débordement négatif")
    max = tab[0]
    tab[0] = tab[n-1]
    Entasser(tab,len(tab),0)
    return max

def inserer(tab,int x):
    global nB
    tab.append(None)
    l=len(tab)-1
    while l == 0 and tab[pere(l)] < x :
        nB += 1
        tab[l] = tab[pere(l)]
        l = pere(l)
    tab[l] = x

def bancEssai2():
    global nB
    """
    Fonction bancEssai2
        Cette fonction effectue des tests.
        Argument[0]:
        Retour : renvoie une courbe avec la fonction afficherCourbe.
    """
    data = []
    for k in range(400,10000):
        nB=0
        f=[]
        inserer(f, 1/2)
        extraireMax(f)
        data.append(nB)
        #shuffle(tab1)

def afficherCourbe(tab,n):
    """
    Fonction afficherCourbe
        Cette fonction affiche une courbe.
        Argument[2]: ES: tab: tableau d'entiers , desc : string.
        Retour : Courbe graphique.
    """
    plot(array(range(len(tab))),array(tab),label=n)

def bancEssai():
    """
    Fonction bancEssai
        Cette fonction effectue des tests.
        Argument[0]:
        Retour : renvoie une courbe avec la fonction afficherCourbe.
    """
    global nB
    #data=[]
    data1=[]
    for k in range(1,1000):
        nB=0
        tab1=[j for j in range(k)]
        temps=tempsMoyen(TrierParTas,tab1,len(tab1),50)
        #shuffle(tab1)
        #ConstruireTas(tab1,k)
        data1.append(temps)
        #data.append(nB)
    #afficherCourbe(data,"tab")
    afficherCourbe(data1,"temps")

def tempsMoyen(fonction,tab,n,nbRepetitions):
    """
    Fonction tempsMoyen
        Cette fonction effectue des tests.
        Argument[4]: fonction, 
        Retour : Entier.
    """
    somme=0
    for k in range(nbRepetitions):
        shuffle(tab)
        start=time.time()
        fonction(tab,n)
        end=time.time()
        somme+=(end-start)
    return somme/nbRepetitions

#run

"""
t1=[6, 28, 22, 24, 18, 0, 21, 22, 4, 17]
verifierProprieteDeTas(t1)
afficherCourbe(t1,"construireTas")
tab1=[j for j in range(100)]
tempsMoyen(TrierParTas,tab1,20,50)
"""
#bancEssai()
bancEssai2()
show()
