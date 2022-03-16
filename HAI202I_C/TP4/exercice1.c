#include <stdio.h>
#include "parfait.h"

int main() {
  int choix, n, a, b, d ;
  printf("Entrer un entier entre 0 et 4 : ") ;
  scanf("%d",&choix) ;
  while (choix!=0) {
    if (choix==1) {
      printf("Entrer un entier : ") ;
      scanf("%d",&n) ;
      printf("%d %s parfait.\n", n, parfait(n)?"est":"n'est pas") ; }
    else if (choix==2) {
      printf("Entrer deux entiers a et b : ") ;
      scanf("%d%d", &a, &b) ;
      n = 0 ;
      for (int i=a ; i<=b ; i++) if (parfait(i)) n++ ;
      printf("%d nombre parfaits dans cet intervalle.\n",n) ; }
    else if (choix==3) {
      printf("Entrer un entier : ") ;
      scanf("%d",&n) ;
      a = 0 ;
      b = 0 ; 
      while (a<n) {
	b++ ;
	if (parfait(b)) a++ ; }
      printf("Le %d-ième nombre parfait est %d.\n", n, b) ; }
    else if (choix==4) {
      printf("Entrer deux entiers n et d (d<n) :") ;
      scanf("%d%d",&n,&d) ;
      a = 0 ;
      while (a<=d && !parfait(n+a) && !parfait(n-a))
	a++ ;
      if (a>d) printf("Non trouvé.\n") ;
      else printf("%d",parfait(n+a)?n+a:n-a) ; }      
    printf("Entrer un entier entre 0 et 4 : ") ;
    scanf("%d",&choix) ;}
  return 0 ; }
