/*  tp1_exo1.c 
    Compiler avec : 
    gcc -Wall tp1_exo1.c -o tp1_exo1
*/

#include <stdio.h>

int main()
{
    int a,b;
    printf("Donnez moi les deux valeur : ");
    scanf("%d%d",&a,&b);
    printf("%d\n",a+b);
    return 0;
}