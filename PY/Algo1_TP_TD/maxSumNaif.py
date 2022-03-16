from random import *
from pylab import *
from math import *

def maxSumNaif(liste):
    nbIterations=0
    somMax,idebut,ifin=liste[0],0,0
    for i in range(len(liste)):
        som=0
    for j in range(i,len(liste)):
        som+=liste[j]
        nbIterations+=1
        if som>somMax :
            somMax,idebut,ifin=som,i,j
    return somMax,liste[idebut:ifin+1],nbIterations