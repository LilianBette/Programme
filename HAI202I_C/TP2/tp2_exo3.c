/*  tp2_exo3.c 
    Compiler avec : 
    gcc -Wall tp2_exo3.c -o tp2_exo3
*/
#include <stdio.h>

int main() {
    float x, puissance=1 ;
    int n ;
    printf("Entrer 2 entiers : ");
    scanf("%d%d",&x,&n);
    for (int i=0 ; i<n ; i++)
        puissance = puissance * x ;
    printf("%f ^ %d = %f \n",x,n,puissance);
    return 0;
}