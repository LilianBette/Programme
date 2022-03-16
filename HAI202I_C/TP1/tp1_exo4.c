/*  tp1_exo4.c 
    Compiler avec : 
    gcc -Wall tp1_exo4.c -o tp1_exo4
*/
#include <stdio.h>

int main() {
    int j = 1023;
    char c = 'Z';
    char d = 'X';
    short i = 100;
    printf("i vaut %hd, j vaut %d, c vaut <%c> et d vaut <%c>\n",i,j,c,d);
    printf("Saisir un caractère pour c : ");
    scanf("%c",&c);
    printf("i vaut %hd, j vaut %d, c vaut <%c> et d vaut <%c>\n",i,j,c,d);
    printf("Saisir un entier pour i : ");
    scanf("%hd",&i);
    printf("i vaut %hd, j vaut %d, c vaut <%c> et d vaut <%c>\n",i,j,c,d);
    return 0;
}