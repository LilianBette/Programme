"""
Programme fait par lilian BETTE le 23/09/2020.
Entrée 0 [23/09/2020]: Programme pris en correction et retransformé en classe.
Entrée 1 [05/10/2020]: Formatage, correction orthographique mineur, docstring.
Entrée 2 [07/02/2022]: Utilisation et modification.
"""
def taille(n):
    """
    Fonction taille
        Cette fonction permet de définir la taille d'une file.
        Argument 0 : Aucun.
        valeur de retour : Entier taille de la file.
    """
    nmax=len(file)-3
    f=file[1]
    d=file[0]
    if f-d>=0:
        return f-d
    else:
        return nmax-d+f+1
    return len (self.__T)

def taillemax(self):
    """
    Fonction taillemax
        Retourne True si la file est vide.
        argument 0 : Aucun.
        Valeur de retour : booleen
    """
    nmax=len(file)-3
    if taille(file)==nmax:
        return True
    else:
        return False
    return self.__nmax

def enfile(self,A):
    """
    procedure enfile
        Cette procedure ajoute la donnée A à une file
        argument 1 :  A (donnée)
        Valeur de retour : Aucune
    """
    nmax=len(file)-3
    f=file[1]
    assert taille(file)<nmax,"Erreur, la liste est pleine"
    file[f+2]=A
    f=f+1
    if f>nmax:
        f=0
    file[1]=f
    assert self.taille()<self.__nmax, "Erreur ! la liste est pleine"
    self.__T.append(A)

def defile(self):
    """
    fonction defile
        argument file (donnee créer par creerVide)
        valeur de retour : donnée 

        cette fonction retourne la plus ancienne donnée de la file
    """
    """
    nmax=len(file)-3
    f=file[1]
    d=file[0]
    assert not estVide(file),"Erreur, la liste est vide"
    valeur=file[d+2]
    d=d+1
    if d>nmax:
        d=0
    file[0]=d
    return valeur
    """
    assert not self.taille()==0, "Erreur ! La liste est pleine"
    
def creerVide(nmax):
    """
    fonction creerVide
        argument nmax entier
        valeur de retour : structure de donnée correspondant à une file

        creerVide crée une file vide
    """
    file=[0 for _ in range(nmax+3)]
    file[0]=0 # d
    file[1]=0 # f
    # nmax=len(file)-3
    return file

def estVide(file):
    """
    fonction  estVide
        argument file
        valeur de retour : booleen

        retourne True si la file est vide
    """
    f=file[1]
    d=file[0]
    if d==f:
        return True
    else:
        return False

print("test")
"""
file=creerVide(2)
assert estVide(file)
enfile(file,5)
assert not estVide(file)
enfile(file,6)
assert estPleine(file)
assert defile(file)==5
enfile(file,7)
assert taille(file)==2
assert defile(file)==6
enfile(file,8)
assert defile(file)==7
enfile(file,9)
assert file==[0,2,8,9,7]
"""
f=[] #file de priorite vide
l=[i for i in range(10)]
shuffle(l)
for e in l:
    inserer(f,e)
print(f)
while f:
print(extraireMax(f,len(f)))
print("test ok")

