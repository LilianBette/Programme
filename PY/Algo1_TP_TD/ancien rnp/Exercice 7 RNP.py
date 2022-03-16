from math import *

print ("Entrer les valeurs de a, b, c de l'equation aX**2+bX+C=0")
a=float(input("Valeur de a : " ))
b=float(input("Valeur de b : " ))
c=float(input("Valeur de c : " ))
print("Resolution de ",a,"X**2 + ",b,"X+ ",c," = 0")
disc = b**2-4*a*c
print("Valeur du discriminant :", disc)
if disc >= 0:
    sol1 = (-b-sqrt(disc))/(2*a)
    sol2 = (-b+sqrt(disc))/(2*a)
    print("Les solutions sont ",sol1," et ",sol2)
else :
    "Erreur algorithme."

