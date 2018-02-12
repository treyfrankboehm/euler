#include <stdio.h>
#include <math.h>
#include "Euler.h"

int isAbundant(int num)
{
    return (num < sumFactor(num));
}

int sumFactor(int num)
{
    int sum = 1;
    int factor, cofactor;
    for (factor = 2; factor <= sqrt(num); factor++) {
        if (num % factor == 0) {
            cofactor = num / factor;
            sum += factor;
            /* Add on the complement unless it's a square root */
            if (cofactor != factor) {
                sum += cofactor;
            }
        }
    }
    return sum;
}

