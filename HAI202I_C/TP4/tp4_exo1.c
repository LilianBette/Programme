/*  tp4_exo1.c 
    Compiler avec : 
    gcc -Wall tp4_exo1.c -o tp4_exo1
*/
//
// Created by Nathael Bonnal on 16/02/2022.
//

#include "parfait.h"
#include <stdbool.h>
#include <stdio.h>
#include "temps.h"

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
            printf("Le nombre %d est parfait", &a);
        } else {
            printf("Il n'y a aucun nombre parfait entre [%d-%d]", &a,&b);
        }
    }
    if (a>b) {
        printf("Le nombre a:%d doit être plus petit que le nombre b:%d", &a, &b);
        intervalPerfectNumberSize();
    }
    for (int i = a; i <= b; ++i) {
        if (verifNumber(i)) {
            counter++;
        }
    }
    printf("Dans l'intervalle [%d-%d] il y a %d nombre parfait", &a, &b, &counter);
}

int keptNumber() {
    int number;
    printf("Saisit un nombre");
    scanf("%d", &number);
    if (number < 0) keptNumber();

    return number;
}

void console() {
    int number;
    printf("0 - quitte le programme\n" "1 - saisit un entier et dit si il est parfait\n" "2 - saisit deux entiers a et b et affiche le nombre d’entiers parfait de l’intervalle [a, b]\n" "3 - saisit un entier n et affiche le ni`eme nombre parfait.\n" "4 - saisit deux entiers n et d, et affiche le plus proche parfait de n s’il en existe un dans l’intervalle" "[n − d, n + d] ou un message d’absence sinon.");

    scanf("%d", &number);


    if (number == 0) {
        return;
    } if (number == 1) {
        int a = keptNumber();
        if (verifNumber(a)) {
            printf("Le nombre: %d est bien parfait", &a);
        } else {
            printf("Le nombre: %d n'est pas parfait", &a);
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

int main() {
    console();
    return 0;
}