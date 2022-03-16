def triInsertion (t):
    tab=list(t)
    print(tab)
    n=len(tab)
    for i in range (1,n):
        x=tab[i]
        j=i-1
        while (j>=0) and (x<tab[j]):
            tab[j+1]=tab[j]
            j=j-1
        tab[j+1]=x
    return tab

def rechercheDichotomique(liste,x):
    if len(liste)==1:
        return liste[0]==x,1
    mid=int(len(liste)/2)
    if liste[mid]==x :
        return True,1
    elif liste[mid]>x :
        a,b=rechercheDichotomique(liste[:mid],x)
        return a,b+1
    else:
        a,b=rechercheDichotomique(liste[mid:],x)
        return a,b+1

def tri_insertiondicho(r):
    tab=list(r)
    print(tab)
    n=len(tab)
    for i in range(1,n):
        x=tab[i]
        j=i-1
        rechercheDichotomique(r,tab[0])
        while (j>=0) and (x<tab[j]):
            tab[j+1]=tab[j]
            j=j-1
        tab[j+1]=x
    return tab

def fusion(T1,T2):
    t=[]
    n1,n2 = len(T1),len(T2)
    i1,i2 = 0 , 0 
    while i1<n1 and i2 < n2 :
        if T1[i1]< T2[i2] : t.append(T1[i1]) ; i1+=1
        else : t.append(T2[i2]) ; i2 += 1
    while i1 < n1 : t.append(T1[i1]) ; i1 += 1
    while i2 < n2 : t.append(T2[i2]) ; i2 += 1
    return (t)

def triFusion(T):
    if len(T)<2 : return T
    else:
        t1 = T[:len(T)//2]
        t2 = T[len(T)//2:len(T)]
        return (fusion(triFusion(t1),triFusion(t2)))

#run
liste=[34,12,9,10,7]
print(triInsertion(liste))
print(tri_insertiondicho(liste))
#triFusion
print ("Test fusion.")
print(triFusion(liste))
print ("Fin test.")
