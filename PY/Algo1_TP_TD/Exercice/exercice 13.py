def ackermann(m,n):
    
    if m == 0 :
        if verbose :
            print (n+1)
        return n+1
    elif  n == 0 :
        if verbose :
            print ("ackermann( ,)" ( m - 1, 1) )                                        
        return ackermann(m-1, 1)
    else :
        if verbose :
            print ("ackerman(,), ackermann(,)" (m - 1, m, n - 1) ) 
        return ackermann(m - 1,ackermann(m, n - 1)) 

print(ackermann(3, 5))