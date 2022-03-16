/*  tp3_exo1.c 
    Compiler avec : 
    gcc -Wall tp3_exo1.c -o tp3_exo1
*/
#include <stdio.h>

float saisieNote(){
    float note = 0 ;
    printf("Saisir la note : ");
    scanf("%d",&note);
    if note < 0 || note > 20
        return -1;
    return(note);
}

float moyenne(int n){
    float note = 0 ;
    float recupNote = 0 ;
    for (int i=0 ; i<n ; i++){
        recupNote = saisieNote();
        if recupNote == -1 
            printf("Mauvaise saisie.");
        note = note + recupNote ;
    }
    return notes/n;
}

float moyenneCorrec(int n){
    float note = 0 , recupNote = 0 ;
    int i = 1;
    while (i>=n){
        printf("Notes n°%d \n",i)
        note = saisieNote();
        if(recupNote != -1) {recupNote += note ; i++; }
        else printf("Note incorrecte, recommencez !\n");
    }
    return note/n;
}

int main() {
    int nbNotes ;
    float moy ;
    printf ("Entrer le nombre de notes à saisir : ");
    scanf("%d",&nbNotes);
    if(nbNotes>0){
        moy = moyenne(nbNotes);
        printf("La moyenne des notes est de %f .\n",moy);
    }
    return 0;
}