#include <stdio.h>
#include "LIB_bette"
#include <math.h>

struct coord3D {
    float x;
    float y;
    float z;
};

double sqr(double a) {
    return a*a;
}

int calculFloat(float x, float y) {
    float somme = x+y;
    float produit = x*y;
    float difference = x-y;
    float quotient;
    if (y!=0){
        quotient = x/y;
        return 1;
    }
    else return 0;
}

double Distance(coord3D A1, coord3D A2) {
    return sqrt(sqr(A1.x - A2.x) + sqr(A1.y - A2.y)) +sqr(A1.z - A2.z); 