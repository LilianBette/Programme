/*  tp1_exo3.c 
    Compiler avec : 
    gcc -Wall tp1_exo3.c -o tp1_exo3
*/

#include <stdio.h>

int main()
{
    printf("Donnez moi le farenheit en relatif: ");
    float a,b;
    scanf("%f",&a);
    b=(a-32.0)/1.8;
    printf("Voici la conversion: ");
    printf("%f\n",b);
    return 0;
}