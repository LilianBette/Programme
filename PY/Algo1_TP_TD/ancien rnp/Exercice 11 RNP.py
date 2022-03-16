from math import *

n=int(input("Valeur n impaire :"))
calcul = 0
i=1
for i in range (n):
    calcul += i*n
    i=i+2
print ("Somme : ",calcul)

"""
n=int(input("Valeur n :"))
calcul = 0
for i in range (n):
    calcul += n*(2*n+1)-n*(n+1)

print("Somme : ",calcul)
"""