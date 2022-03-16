from pylab import *
from random import *
import time

def afficherCourbe(maListeDeValeurs,name):
    plot(array(range(len(maListeDeValeurs))),array(maListeDeValeurs),label=name)

def secondMaximumV1(uneListe):
    if uneListe[0]>uneListe[1]:
        M,S=uneListe[0],uneListe[1]
    else:
        M,S=uneListe[1],uneListe[0]
    for i in range(2,len(uneListe)):
        if uneListe[i]>M:
        M,S=uneListe[i],M
    elif uneListe[i]>S:
    S=uneListe[i]
    return M,S

def secondMaximumV2(uneListe):
    if uneListe[0]>uneListe[1]:
        M,S=uneListe[0],uneListe[1]
    else:
        M,S=uneListe[1],uneListe[0]
    for i in range(2,len(uneListe)):
        if uneListe[i]>S:
            if uneListe[i]>M:
                M,S=uneListe[i],M
            else:
                S=uneListe[i]
    return M,S

def tempsMoyen(fonction,liste,nbRepetitions=50):
    start=time.time()
    for k in range(nbRepetitions):
        fonction(liste)
    end=time.time()
    return (end-start)/nbRepetitions

def bancEssai():
    n=1000
    data1,data2=[],[]
    for i in range(2,n+1):
        liste=[randint(1,n) for _ in range(i)]
        data1.append(tempsMoyen(secondMaximumV1,liste))
        data2.append(tempsMoyen(secondMaximumV2,liste))
        
afficherCourbe(data1,"V1")
afficherCourbe(data2,"V2")
legend(loc='upper right')
show()

bancEssai()
