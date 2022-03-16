from pylab import *
from random import *

def afficherCourbe(maListeDeValeurs):
    plot(array(range(len(maListeDeValeurs))),array(maListeDeValeurs))
    show()
L=[8,1,2,0,7,52,9,8,4]

def recElem(T):
    if T[0] > T[1]:
        M = T[0]; S = T[1]
    else :
        M = T[1]; S = T[0]
    return (M,S)
    

def recMainElem(T):
    j=3 #solution temporaire de problème syntaxe j=3 dans for
    M=T[0]
    S=T[1]
    for j in range (len(T)) :
        if T[j] > M :
            S = M ; M = T[j]
        elif T[j] > S :
            S = T[j]
    return (M,S)

def recElemAux(T) :
    j=3 #solution temporaire de problème syntaxe j=3 dans for
    M=T[0]
    S=T[1]
    for j in range (len(T)):
        if T[j] > S :
            if T[j] > M :
                S = M ; M = T[j]
            else :
                S = T[j]
    return(M,S)

def tempsMoyen(fonction,liste,nbRepetitions=50):
    start=time.time()
    for k in range(nbRepetitions):
        fonction(liste)
    end=time.time()
    return (end-start)/nbRepetitions

#run
print (recElem(L))
print (recMainElem(L))
print (recElemAux(L))

print (tempsMoyen(recElem,L,50))
print (tempsMoyen(recMainElem,L,50))
print (tempsMoyen(recElemAux,L,50))
"""
start=time.time()#compte le temps
t=[randint(1,100) for i in range(10)]
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
"""