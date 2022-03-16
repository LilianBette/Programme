/*  tp2_exo2.c 
    Compiler avec : 
    gcc -Wall tp2_exo2.c -o tp2_exo2
*/
#include <stdio.h>

int main() {
    int a,b,c ;
    printf("Entrer 3 entiers : ");
    scanf("%d%d%d",&a,&b,&c);
    printf("Le maximum est <%d> \n",a>=b && a>=c ? a : b>=c ? b :c);
    printf("Le maximum est <%d> \n",a<=b && a>=c ? a : b<=c ? b :c);
    return 0;
}