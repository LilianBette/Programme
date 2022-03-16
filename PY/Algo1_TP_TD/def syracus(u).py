
def syracus(u):
    if u % 2 == 0 :
        return u//2
    else:
        return 3*u+1

def print_syracus(u):
    if u == 1 :
        return 1
    else:
        print (u)
        print_syracus(syracus(u))
#print(print_syracus(int(input("Choisissez un nombre u0 : "))))
Gcompte = 0
def count_syracus(u):
    global Gcompte 
    if u == 1:
        pass 
    else :
        Gcompte = Gcompte + 1
        count_syracus(syracus(u))
    return Gcompte


def syracus_with_while(u):
    while u != -1:
        n = int(input("Entrez une nouvelle valeur : "))
        return print_syracus(n) or syracus_with_while(u)
print(syracus_with_while(int(input("Choisissez un nombre u0 : "))))