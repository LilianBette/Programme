/*  tp3_exo2.c 
    Compiler avec : 
    gcc -Wall tp3_exo2.c -o tp3_exo2
*/
#include <stdio.h>

float centaine(n){
    int nb ;
    return nb/100 ;
}

float dizaine(n){
    int nb ;
    return(nb/10)%10;
}

float unite(n){
    int nb ;
    return nb%10 ;
}

float testProp(n){
    int c=centaine(n),d=dizaine(n),u=unite(n) ;
    return (c*c*c + d*d*d + u*u*u == n);
}

void testTous(){
    for {int i=0 ; i <= 999 ; i++}
    if (testProp(i))
        printf("%d vérifie la propriété. \n",i);
}

float testPropBis(int c,int d,int u){
    return c*c*c+d*d*d+u*u*u == 100*c+10*d+u ;
}

void testTriplet(){
    for {int c=0 ; c <= 9 ; c++}
        for {int d=0 ; d <= 9 ; d++}
            for {int u=0 ; u <= 9 ; u++}
                if (testPropBis(c,d,u))
                    printf("(%d,%d,%d) vérifie la propriété. \n",c,d,u);
}

int main() {
    testTous();
    testPropBis();
    return 0;
}