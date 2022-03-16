/*  TP4_exo.c 
    Compiler avec : 
    gcc -Wall TP4_exo.c -o TP4_exo
*/

#include "parfait.h"
#include <stdbool.h>
#include <stdio.h>

bool verifNumber(int n) {
    int a;
    for (int i = 1; i < n ; ++i) {
        if (n%i == 0) {
            a += i;
        }
    }
    if (a==n) {
        return true;
    }
    return false;
}
void intervalPerfectNumberSize() {
    int a = keptNumber();
    int b = keptNumber();
    int counter = 0;
    if (a==b) {
        if (verifNumber(a)) {
            printf("Le nombre %i est parfait", a);
        } else {
            printf("Il n'y a aucun nombre parfait entre [%i-%i]", a,b);
        }
    }
    if (a>b) {
        printf("Le nombre a:%i doit être plus petit que le nombre b:%i", a, b);
        intervalPerfectNumberSize();
    }
    for (int i = a; i <= b; ++i) {
        if (verifNumber(i)) {
            counter++;
        }
    }
    printf("Dans l'intervalle [%i-%i] il y a %i nombre parfait", a, b, counter);
}

int keptNumber() {
    int number;
    printf("Saisit un nombre");
    scanf("%i", &number);
    if (number < 0) keptNumber();

    return number;
}

void console() {
    int number;
    printf("0 - quitte le programme\n""1 - saisit un entier et dit si il est parfait\n""2 - saisit deux entiers a et b et affiche le nombre d’entiers parfait de l’intervalle [a, b]\n""3 - saisit un entier n et affiche le ni`eme nombre parfait.\n""4 - saisit deux entiers n et d, et affiche le plus proche parfait de n s’il en existe un dans l’intervalle""[n − d, n + d] ou un message d’absence sinon.\n");

    scanf("%d", &number);


    if (number == 0) {
        return;
    } if (number == 1) {
        int a = keptNumber();
        if (verifNumber(a)) {
            printf("Le nombre: %i est bien parfait\n", a);
        } else {
            printf("Le nombre: %i n'est pas parfait\n", a);
        }
        console();
    } if (number == 2) {
        intervalPerfectNumberSize();
        console();
    } if (number == 3) {

    } if (number == 4) {

    } else {

    }
}

#include <stdio.h>
#include "parfait.h"

int main () {
    console();
}