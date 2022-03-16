/*  tp3_exo3.c 
    Compiler avec : 
    gcc -Wall tp3_exo3.c -o tp3_exo3
*/
#include <stdio.h>

int bissextile(int a){
    return a % 4 == 0 && (a % 100 != 0 || a % 400 == 0);
}

int dateValide(int j,int m,int a){
    if (a > 1582 && m > 0 && m < 12 ){
        switch (m){
            case (m % 2 != 0 ):
                if (j > 31 && j < 0) 
                    return 0;
            case (m % 2 == 0 ):
                if (j > 30 && j < 0)
                    return 0;
            case (m == 2 && bissextile(a) == 1):
                if (j > 28 && j < 0)
                    return 0;
            case (m == 2 && bissextile(a) == 0 ):
                if (j > 29 && j < 0)
                    return 0;
        }
    }
    else 0 ;
}

int compteJours(int j,int m,int a){
    int  nb,i = 0;
    while (i != m){
        for (int i=0 ; i < m ; i++)
            if (dateValide(j,m,a ) == 1 ){
                switch (i){
                    case (i % 2 != 0 ):
                        if (j > 31 && j < 0) 
                            return nb = nb + 31;
                    case (i % 2 == 0 ):
                        if (j < 30 && j > 0)
                            return nb = nb + 30;
                    case (i == 2 && bissextile(a) == 1):
                        if (j > 28 && j < 0)
                            return nb = nb + 28;
                    case (i == 2 && bissextile(a) == 0 ):
                        if (j > 29 && j < 0)
                            return nb = nb + 29;
                }
            }
    }
    if (nb < 365)
        return nb ;
    else 
        return 0 ;
}

int compteJoursProf(int j, int m , int a ) {
    int nbJours = j;
    for (int i=1 ; i <= m-1 ; i++ )
        nbJours += dateValide(j,m,a);
    return nbJours;
}

int main() {
    int j,m,a ;
    scanf("%d%d%d",&j,&m,&a);
    compteJours( j, m, a);
    return 0;
}