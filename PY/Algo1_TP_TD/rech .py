arr=[2,4,5,8,12,14,17,23,27,32,35,36,39]

def rechercheSequentielle(arr, n, x):
    for i in range(n):
        if x == arr[i]:
            return i
    return -1

# correc prof
def rechercheSequentielleP(arr, n, x):
    i=0
    while T[i] != x:
        i += 1
        if i >= n:
            return -1
    return i

# 2.a Implémenter l’algorithme de la recherche dichotomique.
def rechercheDicho(arr, debut, fin, x , v): 
    indice = -1
    while debut <= fin and indice == -1:
        milieu = (fin + debut) // 2
        if arr[milieu] == v:
            x=milieu
        elif arr[milieu] > v:
            debut = milieu -1
        else :
            fin = milieu +1
    pass

#correc prof
def rechercheDichoP(T, debut, fin, x):
    median = (fin - debut)//2
    if T[median] == x:
        return debut + median
    else:
        if T[median] > x:
            return rechercheDicho(T[debut:median], debut, median, x)
        else :
            return rechercheDicho(T[median:fin], median, fin, x)

#correc correc du prof?
def rechercheDichoP(arr, debut, fin, x):
    milieu = (len(arr))//2
    if arr[milieu] == x:
        return milieu
    else:
        if x < arr[milieu] :
            return rechercheDicho(arr[milieu], debut, fin, x)
        else :
            return rechercheDicho(arr[milieu], debut + milieu, fin, x)


def rechercheSequentielle(liste,x):
    nbIterations=0
    for e in liste:
    nbIterations+=1
    if e==x :
        return True,nbIterations
    return False,nbIterations

def rechercheSequentielle(liste,e):
    nbIterations=0
    while (nbIterations<len(liste) and liste[nbIterations]!=e):
        nbIterations+=1
    return nbIterations<len(liste),nbIterations


def rechercheDichotomique(liste,x):
    if len(liste)==1:
        return liste[0]==x,1
        mid=int(len(liste)/2)
    if liste[mid]==x :
        return True,1
    elif liste[mid]>x :
        a,b=rechercheDichotomique(liste[:mid],x)
        return a,b+1
    else :
        a,b=rechercheDichotomique(liste[mid:],x)
        return a,b+1

if __name__ == "__main__":
    rechercheDicho(arr, 0, 10, 17, )

    from pylab import *

