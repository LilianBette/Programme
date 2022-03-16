def binome(n,p):
    if p == 0 or p == n :
        return 1
    return binome(n-1,p)+binome(n-1,p-1)
"""    
def invNb(n:int):
    return len(str(n))
"""
def nbChibDec(n):
    if n == 0:
        return 0
    else :
        return 1+ nbChibDec(n // 10)
#2
def chifRang(n,k):
    if k == 1:
        return n % 10
    else:
        return chifRang(n//10, k-1)
#3
def somChif(n):
    if n<1:
        return 0
    else :
        return n-((n//10)*10) + somChif(n//10)
#4
def racine (n):
    if n==0 :
        return 0
    else :
        return  racine 


#run
if __name__ == '__main__':
    print(binome(7,4))#34 appel 
    print(nbChibDec(1234))
    print(chifRang(12345,2))#4
    print(somChif(4))


                                                             