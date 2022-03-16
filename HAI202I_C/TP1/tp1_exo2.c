/*  tp1_exo2.c 
    Compiler avec : 
    gcc -Wall tp1_exo2.c -o tp1_exo2
*/

#include <stdio.h>

int main()
{
    int a,b;
    printf("Donnez moi les deux valeurs : ");
    scanf("%d%d",&a,&b);
    printf("%d %d %p %p\n",a,b,&a,&b);
    return 0;
}