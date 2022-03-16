int sommeDivPropres(int n) {
  int somme=0 ;
  for (int i=2 ; i<=n-1 ; i++)
    if (n%i == 0)
      somme += i ;
  return somme ;
}
_Bool parfait(int n) {return sommeDivPropres(n)+1==n ;}
