/*  tp2_exo5.c 
    Compiler avec : 
    gcc -Wall tp2_exo5.c -o tp2_exo5
*/
#include <stdio.h>

int main() {
    float somme=0 ;
    int n, nbvaleurs=0 ;

    printf("Entrer 1 entiers : ");
    scanf("%d",&n);

    while (int i>=0)
    {
        nbvaleurs ++ ;
        somme += n ;
        printf("Entrer 1 entiers  : ") ;
        scanf("%d",&n);
    }

    printf("%d valeurs positives ont été entrées. Leur moyenne vaut %f \n",nbvaleurs,(float)somme/nbvaleurs);

    int m ;
    printf("Entrer 1 entiers : ");
    scanf("%d",&m);
    while (int i>=0){
        moyenne = moyenne + 1 ;
    }

    printf("La moyenne des entiers est : %d \n",moyenne);
    return 0;
}