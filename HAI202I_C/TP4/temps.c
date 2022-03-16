#include "temps.h"

struct tps(int h) // incomplet
struct interv (temps ) //incomplet

void afficheTemps (temps T) {printf("%02d:%02d:%06.3f",T.h,T.m,T.s) ;}
float tempsEnSec (temps T) {return 3600*T.h + 60*T.m + T.s;}
temps secEnTemps (float s){
        temps res = {(int) s / 3600, ((int) s / 60) % 60, % - (int)s/60*60};
        return //incomplet
    }
temps duree 

//incomplet