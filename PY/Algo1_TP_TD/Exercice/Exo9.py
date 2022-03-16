from pylab import *
from random import *

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

start=time.time()#compte le temps
t= [randint(1,100) for i in range(10)]
start1=time.time()
(a1,b1,c1)=version1(t)
print(1000*(time.time()-start1))
start2=time.time
(a2,b2,c2)=version2(t)
print(1000*(time.time()-start))
print(a1,b1,c1)
print(a2,b2,c2)
end=time.time
print((end-start)*1000)