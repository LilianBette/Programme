
def degre (p) :
    n = len(p)-1
    while n>-1 and p[n]==0 : 
        n=n-1
    return n

def valPoly(n , p):
    d=degre(p)
    v = 0
    for i in range (d, -1, -1):
        v=v*x+p[i]
    return v

def somPol (p1, p2):
    n1 = degre(p1)
    n2 = degre(p2)
    res = []
    if n2<n1 : 
        return somPol(p2,p1)
    else :
        for i in range(n1+1):
            res.append(p1[i]+p2[i])
        for i in range (n1+1,n2+1):
            res.append(p2[i])
        return res

def derivePol(p):
    res = []
    for i in range(degre(p)):
        res.append(p[i+1]*(i+1))
    return res
