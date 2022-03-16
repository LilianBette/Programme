/*  tp2_exo4.c 
    Compiler avec : 
    gcc -Wall tp2_exo4.c -o tp2_exo4
*/
#include <stdio.h>

int main() {
    float somme=0 ;
    int n ;
    printf("Entrer 1 entiers : ");
    scanf("%d",&n);
    for (int i=1 ; i<=n ; i++)
        somme = somme + 1.0/i ;
    printf("La somme à l'endroit vaut %f \n",somme);
    somme = 0;
    for (int i=n ; i<=1 ; i--)
        somme = somme + 1.0/i ;
    printf("La somme à l'envers vaut %f \n",somme);
    return 0;
}