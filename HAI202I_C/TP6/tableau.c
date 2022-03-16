#include <stdio.h>
#include <stdlib.h>
#define TAILLE 5

int * lireTableau(int n);
int * extraitPairs(int *T, int n, int * nbPairs) ;

int * lireTbleau(int n) {
    int * T = (int*)) malloc(n*sizeof(int));
    for(int i=0;i<n;i++) {
        printf("Entrer T[%d] : ",i) ;
        scanf("%d",&T[i]) ;
    }
    return T ;
}

/*
int t[TAILLE]={4,3,1,8,6} ;
int i;
printf ("[");
for (i=0; i<TAILLE ; i++){
if (i==0) printf("%d" ,t[i]) ;
else printf(",%d",t[i]) ;
}
printf ("]\n") ;
return 0 ; */
