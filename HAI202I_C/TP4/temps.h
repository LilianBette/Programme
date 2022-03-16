#ifndef TEMPS
#define TEMPS

typedef struct tps temps ;
typedef struct interv intervalle ;

void  afficheTemps (tmps T);
float tempsEnSec (temps T);
temps secEnTemps(float s);
temps duree (temps T1, temps T2) ; 
void intervalleV1 (temps depart,temps duree, float coef, temps* tMin, temps*tMax);
temps intervalleV2 (temps depart, temps duree, float coef, temps* tMin);
intervalle intervalleV3 (temps depart, temps duree, float coef) ;

#endif