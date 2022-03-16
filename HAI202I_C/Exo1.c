/*
Programme fait par lilian bette le 07 03 2022.
gcc -Wall Exo1.c -o Exo1
J'ai ouvert le mauvais contrôle, puis j'ai remarqué avec vous que c'était le mauvais tp .
*/
#include <stdio.h>

void pyram1(int n) {
    int i, j;
    for (i = n; i >= 0; --i) { // tous modification des 2 et 3 provoque une boucle infini.
        for (j = n-1; j >= i; --j) {// tous modification des 2 et 3 provoque une boucle infini.
            printf("+");
        }
        printf("\n");
    }
}

void pyram2(int n){
    int i, j, r=0;
    for(i = n; i>=1; i--) //...
    {
        for(j=1; j<=r; j++) 
        printf(" ");
        for(j=1; j<=i; j++) 
        printf("+");
        for(j=i-1; j>=1; j--)
        printf("+");
        printf("\n");
        r++ ;
    }
}

int main() {
    int n;
    printf("Rentrer le nombre d'étages : ");
    scanf ("%d", &n);
    while (n<0){
        printf("Rentrer une valeur positive : ");
        scanf ("%d",&n);
    }
    pyram1(n);
    printf("Deuxième pyramide \n");
    pyram2(n);
    return 0 ;
}